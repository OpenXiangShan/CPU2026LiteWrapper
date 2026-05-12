#!/usr/bin/env python3
"""
Parse SPEC CPU2026 .pm files and generate CPU2026LiteWrapper benchmark directories.
Each benchmark gets: Makefile, run-test.sh, run-train.sh, run-refrate.sh
"""

import os
import re
import sys
import struct
import glob
import subprocess

SPEC_DIR = "/mnt/localdata/spec26/install"
WRAPPER_DIR = "/mnt/localdata/spec26/CPU2026LiteWrapper"
BENCHSPEC = os.path.join(SPEC_DIR, "benchspec", "CPU")

# Byte order detection (matching Perl's Config{byteorder})
def get_byteorder():
    if sys.byteorder == 'little':
        if struct.calcsize('P') == 8:
            return '12345678'
        return '1234'
    else:
        if struct.calcsize('P') == 8:
            return '87654321'
        return '4321'

BYTEORDER = get_byteorder()

def filename_safe_string(s, maxlen=200):
    """Replicate SPEC's filename_safe_string: replace non-[a-zA-Z0-9_.-] with _."""
    result = re.sub(r'[^a-zA-Z0-9_.-]', '_', s)
    return result[:maxlen]

def _scan_fortran_statements(filepath):
    """Scan a file for Fortran MODULE and USE statements, returns (mods_defined, mods_used, includes)."""
    mods_defined = set()
    mods_used = set()
    includes = set()
    try:
        with open(filepath, 'r', errors='replace') as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith('!'):
                    continue
                upper = stripped.upper()
                m = re.match(r'^\s*MODULE\s+(\w+)', upper)
                if m and m.group(1) != 'PROCEDURE':
                    mods_defined.add(m.group(1).lower())
                m = re.match(r'^\s*USE\s+(\w+)', upper)
                if m:
                    mods_used.add(m.group(1).lower())
                # Track #include directives for .h files
                m = re.match(r'^\s*#\s*include\s+["\'<](\S+)["\'>]', stripped)
                if m:
                    includes.add(m.group(1))
    except IOError:
        pass
    return mods_defined, mods_used, includes

def sort_fortran_sources(sources, benchmark):
    """Topologically sort Fortran sources so modules are compiled before their users."""
    src_dir = os.path.join(BENCHSPEC, benchmark, "src")
    if not os.path.isdir(src_dir):
        return sources
    
    fortran_exts = ('.f', '.f90', '.F', '.F90')
    # Separate Fortran from non-Fortran sources
    fortran_srcs = [s for s in sources if any(s.endswith(ext) for ext in fortran_exts)]
    other_srcs = [s for s in sources if not any(s.endswith(ext) for ext in fortran_exts)]
    
    if not fortran_srcs:
        return sources
    
    # Pre-scan all .h files in the source directory for MODULE/USE statements
    h_cache = {}  # header_name -> (mods_defined, mods_used, includes)
    for fname in os.listdir(src_dir):
        if fname.endswith('.h'):
            h_cache[fname] = _scan_fortran_statements(os.path.join(src_dir, fname))
    
    def resolve_includes(direct_includes, visited=None):
        """Recursively resolve all included .h files and collect their MODULE/USE."""
        if visited is None:
            visited = set()
        all_defined = set()
        all_used = set()
        for inc in direct_includes:
            if inc in visited or inc not in h_cache:
                continue
            visited.add(inc)
            hdef, huse, hinc = h_cache[inc]
            all_defined |= hdef
            all_used |= huse
            sub_def, sub_use = resolve_includes(hinc, visited)
            all_defined |= sub_def
            all_used |= sub_use
        return all_defined, all_used
    
    # Scan for MODULE and USE statements, following includes
    provides = {}  # module_name -> source_file
    depends = {}   # source_file -> set of module_names used
    
    for src in fortran_srcs:
        filepath = os.path.join(src_dir, src)
        if not os.path.isfile(filepath):
            continue
        mods_defined, mods_used, includes = _scan_fortran_statements(filepath)
        # Also collect from included headers
        inc_defined, inc_used = resolve_includes(includes)
        mods_defined |= inc_defined
        mods_used |= inc_used
        for mod in mods_defined:
            provides[mod] = src
        depends[src] = mods_used - mods_defined  # Don't depend on self-defined modules
    
    # Topological sort using Kahn's algorithm
    # Build adjacency: src_a -> src_b means src_a must be compiled before src_b
    from collections import deque
    in_degree = {s: 0 for s in fortran_srcs}
    adj = {s: [] for s in fortran_srcs}
    
    for src in fortran_srcs:
        for mod in depends.get(src, set()):
            provider = provides.get(mod)
            if provider and provider != src and provider in in_degree:
                adj[provider].append(src)
                in_degree[src] += 1
    
    queue = deque(s for s in fortran_srcs if in_degree[s] == 0)
    sorted_fortran = []
    while queue:
        node = queue.popleft()
        sorted_fortran.append(node)
        for dep in adj[node]:
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)
    
    # Add any remaining (cyclic deps) at the end
    remaining = [s for s in fortran_srcs if s not in sorted_fortran]
    sorted_fortran.extend(remaining)
    
    return sorted_fortran + other_srcs

# Map benchmark number to its primary executable key in %sources
PRIMARY_EXE = {
    '727': 'cppcheck_r',
    '734': 'vpr',
    '735': 'gem5sim',
    '736': 'ocioperf',
    '753': 'ns3_r',
    '772': 'marian-decoder',
}

def read_pm_file(benchmark):
    """Read and return the full content of a benchmark's object.pm file."""
    pm_path = os.path.join(BENCHSPEC, benchmark, "Spec", "object.pm")
    with open(pm_path, 'r') as f:
        return f.read()

def extract_pm_flags(benchmark):
    """Extract flags and metadata via Perl evaluation of .pm file."""
    bench_path = os.path.join(BENCHSPEC, benchmark)
    extractor = os.path.join(WRAPPER_DIR, "extract_sources.pl")
    
    result_dict = {}
    try:
        result = subprocess.run(
            ["perl", extractor, bench_path, "flags"],
            capture_output=True, text=True, timeout=30
        )
        for line in result.stdout.strip().split('\n'):
            if '=' in line:
                key, _, val = line.partition('=')
                result_dict[key.strip()] = val.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return result_dict

def extract_sources(pm_content, benchmark):
    """Extract source file list from .pm content using Perl evaluation."""
    # Use the Perl extractor for accurate source resolution
    bench_path = os.path.join(BENCHSPEC, benchmark) if benchmark else ""
    extractor = os.path.join(WRAPPER_DIR, "extract_sources.pl")
    
    if benchmark and os.path.isdir(bench_path) and os.path.isfile(extractor):
        try:
            result = subprocess.run(
                ["perl", extractor, bench_path],
                capture_output=True, text=True, timeout=30
            )
            lines = [l.strip() for l in result.stdout.strip().split('\n') if l.strip()]
            if lines:
                # Check if multi-exe format (exe:source)
                if ':' in lines[0]:
                    multi = {}
                    for line in lines:
                        exe, src = line.split(':', 1)
                        if exe not in multi:
                            multi[exe] = []
                        if src not in multi[exe]:
                            multi[exe].append(src)
                    return None, multi
                else:
                    # Deduplicate preserving order
                    seen = set()
                    deduped = []
                    for s in lines:
                        if s not in seen:
                            seen.add(s)
                            deduped.append(s)
                    return deduped, None
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
    
    # Fallback: regex extraction
    return _extract_sources_regex(pm_content)


def _extract_sources_regex(pm_content):
    """Fallback regex-based source extraction."""
    sources = []
    
    # Check for %sources (multi-exe)
    multi_exe_sources = {}
    msrc_match = re.search(r'%sources\s*=\s*\((.+?)\);', pm_content, re.DOTALL)
    if msrc_match:
        block = msrc_match.group(1)
        exe_pattern = re.finditer(r"'(\w[\w-]*)'\s*=>\s*\[\s*qw\((.+?)\)\s*\]", block, re.DOTALL)
        for m in exe_pattern:
            exe_name = m.group(1)
            files = m.group(2).split()
            multi_exe_sources[exe_name] = files
        if multi_exe_sources:
            return None, multi_exe_sources
    
    # Standard @sources = qw( ... );
    match = re.search(r'@sources\s*=\s*qw\((.+?)\);', pm_content, re.DOTALL)
    if match:
        sources = match.group(1).split()
        return sources, None
    
    # @sources = ( qw( ... ) );
    match = re.search(r'@sources\s*=\s*\(qw\((.+?)\)\s*\);', pm_content, re.DOTALL)
    if match:
        sources = match.group(1).split()
        return sources, None
    
    # @sources = (qw(...), qw(...)); or mixed patterns
    match = re.search(r'@sources\s*=\s*\((.+?)\);', pm_content, re.DOTALL)
    if match:
        block = match.group(1)
        for qw_match in re.finditer(r'qw\((.+?)\)', block, re.DOTALL):
            sources.extend(qw_match.group(1).split())
        for q_match in re.finditer(r"'([^']+\.\w+)'", block):
            if q_match.group(1) not in sources:
                sources.append(q_match.group(1))
        return sources, None
    
    return sources, None

def extract_exename(pm_content):
    """Extract the executable name."""
    match = re.search(r"\$exename\s*=\s*'([^']+)'", pm_content)
    if match:
        return match.group(1)
    return None

def extract_benchlang(pm_content):
    """Extract the benchmark language."""
    match = re.search(r"\$benchlang\s*=\s*'([^']+)'", pm_content)
    if match:
        return match.group(1)
    return None

def extract_base_exe(pm_content):
    """Extract base_exe list."""
    # @base_exe = qw/exe1 exe2/;
    match = re.search(r'@base_exe\s*=\s*qw[/|]([\w\s_-]+)[/|]', pm_content)
    if match:
        return match.group(1).split()
    # @base_exe = ($exename);
    match = re.search(r'@base_exe\s*=\s*\(\$exename\)', pm_content)
    if match:
        exename = extract_exename(pm_content)
        return [exename] if exename else []
    # @base_exe = (qw/exe1 exe2/);
    match = re.search(r'@base_exe\s*=\s*\(qw[/|]([\w\s_-]+)[/|]\)', pm_content)
    if match:
        return match.group(1).split()
    return []

def fix_include_paths(flags):
    """Prefix relative -I paths with src/ since sources live under src/."""
    parts = flags.split()
    result = []
    i = 0
    while i < len(parts):
        if parts[i].startswith('-I') and len(parts[i]) > 2:
            path = parts[i][2:]
            if not path.startswith('/'):
                result.append(f'-Isrc/{path}')
            else:
                result.append(parts[i])
        elif parts[i] == '-I' and i + 1 < len(parts):
            path = parts[i + 1]
            if not path.startswith('/'):
                result.append('-I')
                result.append(f'src/{path}')
            else:
                result.append(parts[i])
                result.append(parts[i + 1])
            i += 1
        else:
            result.append(parts[i])
        i += 1
    return ' '.join(result)

def extract_bench_flags(pm_content):
    """Extract benchmark-specific flags."""
    flags = ""
    
    # Strip Perl comment lines before extracting flags
    active_lines = []
    for line in pm_content.split('\n'):
        stripped = line.lstrip()
        if not stripped.startswith('#'):
            active_lines.append(line)
    active_content = '\n'.join(active_lines)
    
    # Extract $bench_flags
    # Handle multi-line concatenation
    for match in re.finditer(r"\$bench_flags\s*\.?=\s*'([^']*)'", active_content):
        flags += " " + match.group(1)
    for match in re.finditer(r'\$bench_flags\s*\.?=\s*"([^"]*)"', active_content):
        flags += " " + match.group(1)
    # Handle join() patterns
    for match in re.finditer(r"\$bench_flags\s*\.?=\s*'\s*'\s*\.join\(\s*'\s*',\s*qw\((.+?)\)\)", active_content, re.DOTALL):
        flags += " " + " ".join(match.group(1).split())
    
    # Handle $Config{'byteorder'} concatenation:
    # Pattern: '-DSPEC_AUTO_BYTEORDER=0x'.$Config{'byteorder'}
    flags = re.sub(r"-DSPEC_AUTO_BYTEORDER=0x\b", f"-DSPEC_AUTO_BYTEORDER=0x{BYTEORDER}", flags)
    
    # Extract $bench_cxxflags
    for match in re.finditer(r"\$bench_cxxflags\s*\.?=\s*['\"]([^'\"]*)['\"]\.", active_content):
        flags += " " + match.group(1)
    
    # Fix -I paths to be relative to src/
    flags = fix_include_paths(flags)
    
    return flags.strip()

def extract_need_math(pm_content):
    """Check if -lm is needed."""
    match = re.search(r"\$need_math\s*=\s*'yes'", pm_content)
    return match is not None

def extract_tolerances(pm_content):
    """Extract tolerance settings."""
    tols = {}
    
    # Simple scalar tolerances
    match = re.search(r"\$abstol\s*=\s*([\d.eE+-]+)\s*;", pm_content)
    if match:
        tols['abstol'] = match.group(1)
    
    match = re.search(r"\$reltol\s*=\s*([\d.eE+-]+)\s*;", pm_content)
    if match:
        tols['reltol'] = match.group(1)
    
    match = re.search(r"\$calctol\s*=\s*0\s*;", pm_content)
    if match:
        tols['calctol'] = '0'
    
    match = re.search(r"\$floatcompare\s*=\s*1\s*;", pm_content)
    if match:
        tols['floatcompare'] = True
    
    return tols

def get_control_content(benchmark, size):
    """Read the control file for a given size."""
    control_path = os.path.join(BENCHSPEC, benchmark, "data", size, "input", "control")
    if os.path.exists(control_path):
        with open(control_path, 'r') as f:
            return f.read()
    return None

def get_output_files(benchmark, size):
    """List output files for a given size."""
    output_dir = os.path.join(BENCHSPEC, benchmark, "data", size, "output")
    if os.path.exists(output_dir):
        return sorted(os.listdir(output_dir))
    return []

def parse_control_lines(control_content):
    """Parse control file, skipping comments and blank lines."""
    if not control_content:
        return []
    lines = []
    for line in control_content.strip().split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            lines.append(line)
    return lines

def generate_run_script(benchmark, pm_content, size):
    """Generate the run script for a given benchmark and size."""
    exename = extract_exename(pm_content)
    benchname = benchmark.split('.')[1]
    
    # Get control content
    control = get_control_content(benchmark, size)
    control_lines = parse_control_lines(control)
    
    lines = []
    
    # Different invoke patterns per benchmark
    benchnum = benchmark.split('.')[0]
    
    if benchnum == '782':  # lbm_r - reads from .in file
        in_path = os.path.join(BENCHSPEC, benchmark, "data", size, "input", "lbm.in")
        if os.path.exists(in_path):
            with open(in_path) as f:
                args = f.read().strip()
        else:
            args = ""
        name = "lbm"
        lines.append(f"$APP {args} > {name}.out 2> {name}.err")
    
    elif benchnum == '706':  # stockfish_r - control file args
        for cl in control_lines:
            args = cl.strip()
            # Parse fen name and algo from the line
            parts = args.split()
            # Find .fen file and algo (last arg)
            fen = None
            algo = parts[-1] if parts else ""
            for p in parts:
                if p.endswith('.fen'):
                    fen = p.replace('.fen', '')
                    break
            if fen:
                lines.append(f"$APP {args} > {exename}_{fen}_{algo}.out 2> {exename}_{fen}_{algo}.err")
            else:
                lines.append(f"$APP {args} > {exename}.out 2> {exename}.err")
    
    elif benchnum == '707':  # ntest_r - control: file h1 h2
        for cl in control_lines:
            parts = cl.split()
            if len(parts) >= 3:
                fname, h1, h2 = parts[0], parts[1], parts[2]
                basename = os.path.splitext(fname)[0]
                lines.append(f"$APP {fname} {h1} {h2} > ntest.{basename}.{h1}.{h2}.out 2> ntest.{basename}.{h1}.{h2}.err")
    
    elif benchnum == '708':  # sqlite_r - control file args
        for cl in control_lines:
            args_list = cl.split()
            # testset is args[4]
            testset = args_list[4] if len(args_list) > 4 else "main"
            lines.append(f"$APP {cl} > {exename}.{testset}.out 2> {exename}.{testset}.err")
    
    elif benchnum == '709':  # cactus_r - first line of control
        if control_lines:
            args = control_lines[0]
            lines.append(f"$APP {args} > cactus.out 2> cactus.err")
    
    elif benchnum == '710':  # omnetpp_r - control: configfile configname runnumber
        for cl in control_lines:
            parts = cl.split()
            if len(parts) >= 2:
                configfile = parts[0]
                configname = parts[1]
                lines.append(f"$APP -f {configfile} -c {configname} > omnetpp.{configname}-0.out 2> omnetpp.{configname}-0.err")
    
    elif benchnum == '714':  # cpython_r - control file args, indexed output
        for i, cl in enumerate(control_lines):
            lines.append(f"$APP {cl} > cpython_r_{i}.out 2> cpython_r_{i}.err")
    
    elif benchnum == '721':  # gcc_r - control: file opts
        for cl in control_lines:
            parts = cl.split()
            infile = parts[0]
            opts = " ".join(parts[1:])
            # Perl: filename_safe_string("${src}.opts" . join('_', @opts))
            raw_tag = infile + ".opts" + "_".join(parts[1:])
            outname = filename_safe_string(raw_tag) + ".s"
            lines.append(f"$APP {infile} {opts} -o {outname} > {outname}.out 2> {outname}.err")
    
    elif benchnum == '722':  # palm_r - stdin from runfile_atmos
        lines.append(f"$APP < runfile_atmos > {exename}.out 2> {exename}.err")
    
    elif benchnum == '723':  # llvm_r - control: file opts
        for cl in control_lines:
            parts = cl.split()
            infile = parts[0]
            opts = " ".join(parts[1:])
            # Perl: filename_safe_string("${src}.opts" . join('_', @opts))
            raw_tag = infile + ".opts" + "_".join(parts[1:])
            out = filename_safe_string(raw_tag)
            lines.append(f"$APP {infile} {opts} --sha512 -o {out}.ll > {out}.out 2> {out}.err")
    
    elif benchnum == '727':  # cppcheck_r - control file with --output-file
        for cl in control_lines:
            # Perl: ($mark) = $line =~ /--output-file=(\S+)\.txt/
            match = re.search(r'--output-file=(\S+)\.txt', cl)
            mark = match.group(1) if match else "cppcheck"
            lines.append(f"$APP {cl} --platform=unix64 > cppcheck_r.{mark}.out 2> cppcheck_r.{mark}.err")
    
    elif benchnum == '729':  # abc_r - control: workload names
        for cl in control_lines:
            wkload = cl.split()[0]
            lines.append(f"$APP -F {wkload}.in > {wkload}.out 2> {wkload}.err")
    
    elif benchnum == '731':  # astcenc_r - control file args, indexed output
        for i, cl in enumerate(control_lines):
            lines.append(f"$APP {cl} > {exename}.{i}.out 2> {exename}.{i}.err")
    
    elif benchnum == '734':  # vpr_r - control file args
        for cl in control_lines:
            parts = cl.split()
            # file is args[1], step is last arg minus --
            infile = parts[1] if len(parts) > 1 else "vpr"
            step = parts[-1][2:] if len(parts) > 0 and parts[-1].startswith('--') else parts[-1]
            lines.append(f"$APP {cl} > {infile}.{step}.out 2> {infile}.{step}.err")
    
    elif benchnum == '735':  # gem5_r - control.cmd file
        ctrl_cmd_path = os.path.join(BENCHSPEC, benchmark, "data", size, "input", "control.cmd")
        if os.path.exists(ctrl_cmd_path):
            with open(ctrl_cmd_path) as f:
                cmd_content = f.read()
            for cl in parse_control_lines(cmd_content):
                args_list = cl.split()
                # Perl: filename_safe_string(join('_', @args))
                out = filename_safe_string("_".join(args_list))
                lines.append(f"$APP --stats-file={out}.stats.txt {cl} > {out}.out 2> {out}.err")
        else:
            lines.append(f"$APP > gem5sim.out 2> gem5sim.err")
    
    elif benchnum == '736':  # ocio_r - control: tool args
        for cl in control_lines:
            parts = cl.split()
            tool = parts[0] if parts else "perf"
            rest = " ".join(parts[1:]) if len(parts) > 1 else ""
            # Perl: ($input) = $line =~ /(\/\S+)$/; $input =~ s/\///g;
            imatch = re.search(r'/([^/\s]+)$', cl)
            if imatch:
                inp = imatch.group(1)
                lines.append(f"$APP {rest} > {tool}_{inp}.out 2> {tool}_{inp}.err")
            else:
                lines.append(f"$APP {rest} > {tool}.out 2> {tool}.err")
    
    elif benchnum == '737':  # gmsh_r - control file args
        for cl in control_lines:
            parts = cl.split()
            mesh = parts[0]
            rest = " ".join(parts[1:]) if len(parts) > 1 else ""
            lines.append(f"$APP -option gmsh.opts -nt 0 {cl} > {mesh}.out 2> {mesh}.err")
    
    elif benchnum == '748':  # flightdm_r - control: args with script path
        for cl in control_lines:
            # grab last argument (the script file)
            parts = cl.split()
            infile_match = re.search(r'/(\S+)$', cl)
            infile = infile_match.group(1) if infile_match else parts[-1]
            lines.append(f"$APP {cl} > {infile}.out 2> {infile}.err")
    
    elif benchnum == '749':  # fotonik3d_r - no args
        lines.append(f"$APP > fotonik3d.log 2> fotonik3d.err")
    
    elif benchnum == '750':  # sealcrypto_r - control file args
        for cl in control_lines:
            tag = re.sub(r'[^a-zA-Z0-9.]+', '_', cl.strip())
            tag = tag.strip('_')
            lines.append(f"$APP {cl} > homoencrypt.{tag}.out 2> homoencrypt.{tag}.err")
    
    elif benchnum == '753':  # ns3_r - control: program args
        for i, cl in enumerate(control_lines):
            parts = cl.split()
            prog = parts[0]
            rest = " ".join(parts[1:]) if len(parts) > 1 else ""
            # Perl puts --RngSeed=1 --RngRun=1 at the END of args
            lines.append(f"$APP {cl} --RngSeed=1 --RngRun=1 > {prog}_{i}.out 2> {prog}_{i}.err")
    
    elif benchnum == '765':  # roms_r - .in.x input file
        in_files = glob.glob(os.path.join(BENCHSPEC, benchmark, "data", size, "input", "*.in.x"))
        if in_files:
            for inf in sorted(in_files):
                inname = os.path.basename(inf).replace('.in.x', '')
                lines.append(f"$APP < {inname}.in.x > {inname}.log 2> {inname}.err")
        else:
            lines.append(f"$APP > roms.log 2> roms.err")
    
    elif benchnum == '766':  # femflow_r - .prm parameter file
        prm_files = glob.glob(os.path.join(BENCHSPEC, benchmark, "data", size, "input", "*.prm"))
        if prm_files:
            prm = os.path.basename(sorted(prm_files)[0])
            lines.append(f"$APP {prm} > femflow.out 2> femflow.err")
        else:
            lines.append(f"$APP > femflow.out 2> femflow.err")
    
    elif benchnum == '767':  # nest_r - .sli script files from control
        if control_lines:
            for cl in control_lines:
                sli_file = cl.split()[0]
                lines.append(f"$APP {sli_file} > {sli_file}.out 2> {sli_file}.err")
        else:
            # Fallback: find .sli files
            sli_dir = os.path.join(BENCHSPEC, benchmark, "data", size, "input")
            if os.path.isdir(sli_dir):
                sli_files = sorted([f for f in os.listdir(sli_dir) if f.endswith('.sli')])
                for sf in sli_files:
                    lines.append(f"$APP {sf} > {sf}.out 2> {sf}.err")
    
    elif benchnum == '772':  # marian_r - control file args
        for cl in control_lines:
            # Find the -o flag to get output name
            omatch = re.search(r'-o\s+(\S+)', cl)
            outname = omatch.group(1) if omatch else "marian.out"
            lines.append(f"$APP --cpu-threads 1 {cl} > run_{outname}.out 2> run_{outname}.err")
    
    elif benchnum == '777':  # zstd_r - control file args
        for cl in control_lines:
            tag = re.sub(r'[^a-zA-Z0-9.]+', '_', cl.strip())
            tag = tag.strip('_')
            lines.append(f"$APP {cl} > zstd.{tag}.out 2> zstd.{tag}.err")
    
    else:
        # Generic fallback
        if control_lines:
            for cl in control_lines:
                lines.append(f"$APP {cl} > {exename}.out 2> {exename}.err")
        else:
            lines.append(f"$APP > {exename}.out 2> {exename}.err")
    
    return "\n".join(lines) + "\n"

def determine_linker(pm_content, benchlang, benchmark=""):
    """Determine linker type."""
    if 'Fortran' in (benchlang or '') or benchlang in ('F', 'F90', 'F77'):
        return 'fortran'
    # Check explicit language markers
    lang = benchlang or ''
    if 'CXX' in lang or 'C++' in lang:
        return 'cxx'
    # Check source files for language hints
    sources, multi = extract_sources(pm_content, benchmark)
    if sources:
        has_fortran = any(s.endswith(('.f', '.f90', '.F', '.F90')) for s in sources)
        has_cxx = any(s.endswith(('.cpp', '.cc', '.cxx', '.C')) for s in sources)
        if has_fortran:
            return 'fortran'
        if has_cxx:
            return 'cxx'
    if multi:
        for exe, srcs in multi.items():
            if any(s.endswith(('.cpp', '.cc', '.cxx', '.C')) for s in srcs):
                return 'cxx'
    return 'c'

def generate_makefile(benchmark, pm_content):
    """Generate the Makefile for a benchmark."""
    # Use Perl evaluation for accurate flags
    pm_flags = extract_pm_flags(benchmark)
    
    exename = pm_flags.get('EXENAME') or extract_exename(pm_content)
    benchlang = pm_flags.get('BENCHLANG') or extract_benchlang(pm_content)
    sources, multi_sources = extract_sources(pm_content, benchmark)
    need_math = pm_flags.get('NEED_MATH', '').lower() == 'yes' or extract_need_math(pm_content)
    tols = extract_tolerances(pm_content)
    linker = determine_linker(pm_content, benchlang, benchmark)
    
    # Get flags from Perl (accurate) and apply fix_include_paths
    bench_flags = pm_flags.get('BENCH_FLAGS', '')
    bench_cxxflags = pm_flags.get('BENCH_CXXFLAGS', '')
    bench_fflags = pm_flags.get('BENCH_FFLAGS', '')
    bench_fppflags = pm_flags.get('BENCH_FPPFLAGS', '')
    bench_ldflags = pm_flags.get('BENCH_LDFLAGS', '')
    
    # Fall back to regex extraction if Perl gave nothing
    if not bench_flags and not bench_cxxflags:
        bench_flags = extract_bench_flags(pm_content)
    else:
        bench_flags = fix_include_paths(bench_flags)
        bench_cxxflags = fix_include_paths(bench_cxxflags)
    
    lines = []
    lines.append(f"NAME = {benchmark}")
    
    if multi_sources:
        # Multi-executable benchmark - only use primary exe's sources
        benchnum = benchmark.split('.')[0]
        primary_key = PRIMARY_EXE.get(benchnum)
        if primary_key and primary_key in multi_sources:
            primary_sources = multi_sources[primary_key]
        else:
            # Fallback: use the exe with the most sources
            primary_key = max(multi_sources, key=lambda k: len(multi_sources[k]))
            primary_sources = multi_sources[primary_key]
        
        srcs_str = format_source_list(primary_sources)
        lines.append(f"SRCS = $(addprefix src/,{srcs_str})")
    elif sources:
        # Sort Fortran sources for module dependencies
        sources = sort_fortran_sources(sources, benchmark)
        srcs_str = format_source_list(sources)
        lines.append(f"SRCS = $(addprefix src/,{srcs_str})")
    else:
        lines.append("SRCS =")
    
    # Split flags between C, CXX, Fortran
    c_flags = []
    cxx_flags = []
    f_flags = []
    ld_flags = []
    
    if bench_flags:
        c_flags.append(bench_flags)
    if bench_cxxflags:
        cxx_flags.append(bench_cxxflags)
    if bench_fflags:
        f_flags.append(bench_fflags)
    
    lines.append(f"SPEC_CFLAGS += {' '.join(c_flags)}")
    lines.append(f"SPEC_CXXFLAGS += {' '.join(cxx_flags)}")
    lines.append(f"SPEC_FFLAGS += {' '.join(f_flags)}")
    
    if need_math:
        ld_flags.append("-lm")
    if bench_ldflags:
        ld_flags.append(bench_ldflags)
    
    lines.append(f"SPEC_LDFLAGS += {' '.join(ld_flags)}")
    
    if bench_fppflags:
        lines.append(f"SPECCPPFLAGS += {bench_fppflags}")
    
    if linker == 'cxx':
        lines.append("LD_CXX = 1")
    elif linker == 'fortran':
        lines.append("LD_FORTRAN = 1")
        lines.append(".NOTPARALLEL:")  # Fortran module deps require sequential build
    
    lines.append("include ../Makefile.apps")
    lines.append("include ../Makefile.run")
    lines.append(".PHONY: clean_preprocess_objs")
    lines.append("clean_preprocess_objs:")
    # Clean .fppized files for Fortran sources that need preprocessing
    all_srcs = sources or []
    if multi_sources:
        for s_list in multi_sources.values():
            all_srcs = all_srcs + (s_list or [])
    fpp_srcs = [s for s in all_srcs if s.endswith('.F90') or s.endswith('.F')]
    if fpp_srcs:
        fpp_files = []
        for s in fpp_srcs:
            if s.endswith('.F90'):
                fpp_files.append('src/' + s[:-4] + '.fppized.f90')
            elif s.endswith('.F'):
                fpp_files.append('src/' + s[:-2] + '.fppized.f')
        lines.append(f"\trm -f {' '.join(fpp_files)}")
    lines.append("")
    
    # Generate comparison targets
    for s in ['refrate', 'train', 'test']:
        output_files = get_output_files(benchmark, s)
        if output_files:
            lines.append(f"{s}-cmp:")
            
            specdiff_flags = []
            if tols.get('floatcompare'):
                specdiff_flags.append("--floatcompare")
            if tols.get('abstol'):
                specdiff_flags.append(f"--abstol {tols['abstol']}")
            if tols.get('reltol'):
                specdiff_flags.append(f"--reltol {tols['reltol']}")
            
            if specdiff_flags or tols.get('calctol') == '0':
                if tols.get('calctol') == '0':
                    # No tolerance - use exact diff
                    lines.append(f"\t@for f in {' '.join(output_files)}; do \\")
                    lines.append(f"\t\t$(DIFF) $(RUN_DIR)/$$f data/{s}/output/$$f; \\")
                    lines.append(f"\tdone")
                else:
                    flags_str = " ".join(specdiff_flags)
                    lines.append(f"\t@for f in {' '.join(output_files)}; do \\")
                    lines.append(f"\t\t$(call SPECDIFF, {flags_str}, $(RUN_DIR)/$$f, data/{s}/output/$$f); \\")
                    lines.append(f"\tdone")
            else:
                lines.append(f"\t@for f in {' '.join(output_files)}; do \\")
                lines.append(f"\t\t$(DIFF) $(RUN_DIR)/$$f data/{s}/output/$$f; \\")
                lines.append(f"\tdone")
        else:
            lines.append(f"{s}-cmp:")
            lines.append(f"\t@echo \"No output validation for {benchmark} ({s})\"")
    
    return "\n".join(lines) + "\n"

def format_source_list(sources):
    """Format a source list for Makefile."""
    if len(sources) <= 3:
        return " ".join(sources)
    
    result = sources[0]
    for s in sources[1:]:
        result += " \\\n\t" + s
    return result

def check_has_prepare_data(benchmark, pm_content):
    """Check if the benchmark needs data preparation (e.g., xz decompression)."""
    return 'generate_inputs' in pm_content or 'OBJ-values.dat.xz' in pm_content

def generate_prepare_data_sh(benchmark, pm_content):
    """Generate prepare-data.sh if needed."""
    benchnum = benchmark.split('.')[0]
    
    if benchnum == '749':  # fotonik3d_r
        return """#!/bin/bash
# Decompress OBJ-values.dat.xz for each size
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    if [ -f "${INPUT_DIR}/OBJ-values.dat.xz" ]; then
        echo "Decompressing ${INPUT_DIR}/OBJ-values.dat.xz..."
        xz -dk "${INPUT_DIR}/OBJ-values.dat.xz" 2>/dev/null || true
    fi
done
"""
    
    if benchnum == '734':  # vpr_r - xz decompression
        return """#!/bin/bash
# Decompress .xz files for vpr
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    if [ -d "${INPUT_DIR}" ]; then
        for xzfile in ${INPUT_DIR}/*.xz; do
            [ -f "$xzfile" ] || continue
            echo "Decompressing $xzfile..."
            xz -dk "$xzfile" 2>/dev/null || true
        done
    fi
done
"""
    
    if benchnum == '735':  # gem5_r - xz decompression from control.gen
        return """#!/bin/bash
# Decompress .xz files for gem5
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    GEN_FILE="${INPUT_DIR}/control.gen"
    if [ -f "${GEN_FILE}" ]; then
        while IFS= read -r line; do
            [ -z "$line" ] && continue
            [[ "$line" = \\#* ]] && continue
            xzfile="${INPUT_DIR}/${line}.xz"
            if [ -f "$xzfile" ]; then
                echo "Decompressing $xzfile..."
                xz -dk "$xzfile" 2>/dev/null || true
            fi
        done < "${GEN_FILE}"
    fi
done
"""
    
    return None

def main():
    # Rate benchmarks from the bset files
    intrate = [
        "706.stockfish_r", "707.ntest_r", "708.sqlite_r", "710.omnetpp_r",
        "714.cpython_r", "721.gcc_r", "723.llvm_r", "727.cppcheck_r",
        "729.abc_r", "734.vpr_r", "735.gem5_r", "750.sealcrypto_r",
        "753.ns3_r", "777.zstd_r"
    ]
    fprate = [
        "709.cactus_r", "722.palm_r", "731.astcenc_r", "736.ocio_r",
        "737.gmsh_r", "748.flightdm_r", "749.fotonik3d_r", "765.roms_r",
        "766.femflow_r", "767.nest_r", "772.marian_r", "782.lbm_r"
    ]
    
    all_benchmarks = intrate + fprate
    
    for benchmark in all_benchmarks:
        print(f"Processing {benchmark}...")
        bench_dir = os.path.join(WRAPPER_DIR, benchmark)
        os.makedirs(bench_dir, exist_ok=True)
        
        pm_content = read_pm_file(benchmark)
        
        # Generate Makefile
        makefile = generate_makefile(benchmark, pm_content)
        with open(os.path.join(bench_dir, "Makefile"), 'w') as f:
            f.write(makefile)
        
        # Generate run scripts
        for size in ['test', 'train', 'refrate']:
            script = generate_run_script(benchmark, pm_content, size)
            script_path = os.path.join(bench_dir, f"run-{size}.sh")
            with open(script_path, 'w') as f:
                f.write(script)
        
        # Generate prepare-data.sh if needed
        prep = generate_prepare_data_sh(benchmark, pm_content)
        if prep:
            prep_path = os.path.join(bench_dir, "prepare-data.sh")
            with open(prep_path, 'w') as f:
                f.write(prep)
    
    print(f"\nDone! Generated {len(all_benchmarks)} benchmark directories.")

if __name__ == '__main__':
    main()
