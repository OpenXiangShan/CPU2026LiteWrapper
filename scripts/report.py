import argparse
import os

verbose = False

def get_spec_int():
  return [
    "706.stockfish_r",
    "707.ntest_r",
    "708.sqlite_r",
    "710.omnetpp_r",
    "714.cpython_r",
    "721.gcc_r",
    "723.llvm_r",
    "727.cppcheck_r",
    "729.abc_r",
    "734.vpr_r",
    "735.gem5_r",
    "750.sealcrypto_r",
    "753.ns3_r",
    "777.zstd_r",
  ]

def get_spec_fp():
  return [
    "709.cactus_r",
    "722.palm_r",
    "731.astcenc_r",
    "736.ocio_r",
    "737.gmsh_r",
    "748.flightdm_r",
    "749.fotonik3d_r",
    "765.roms_r",
    "766.femflow_r",
    "767.nest_r",
    "772.marian_r",
    "782.lbm_r",
  ]

def get_ref_time(benchspec, input):
  spec_dir = os.getenv('SPEC')
  if spec_dir is None:
    print("Please set SPEC environment variable.")
    exit()
  bench_dir = os.path.join(spec_dir, "benchspec", "CPU", benchspec)
  reftime_path = os.path.join(bench_dir, "data", input, "reftime")
  f = open(reftime_path)
  reftime = None
  for line in f.readlines():
      cur_input, input_type, cur_reftime = line.split()
      if cur_input == input:
          reftime = float(cur_reftime)
  f.close()
  return reftime

def get_run_time(benchspec, input, run_tag):
  elapsed_time = 0
  log_path = os.path.join(benchspec, f"run{run_tag}", f"run-{input}.sh.timelog")
  if not os.path.exists(log_path):
    if verbose:
      print(f"Does not find {log_path} for {benchspec}. Use REFTIME instead.")
    return get_ref_time(benchspec, input)
  with open(log_path, "r") as f:
    for line in f:
      if "elapsed in second" in line:
        elapsed_time += float(line.split("#")[0].strip())
  return elapsed_time

def report(input, fp_case, int_case, run_tag):
  def bold(s, replace_slash=True):
    if not replace_slash:
        return '\033[1m' + s + '\033[0m'
    else:
        return "|".join(map(lambda x: bold(x, False), s.split("|")))

  def report_partial(name, benchspecs):
    spec_score = 1
    for benchspec in benchspecs:
      ref_time = get_ref_time(benchspec, input)
      run_time = get_run_time(benchspec, input, run_tag)
      score = ref_time / run_time
      spec_score *= score
      print(f"| {benchspec:15}| {ref_time:8.2f} | {run_time:8.2f} | {score:5.2f} |")
    geomean_spec_score = spec_score ** (1 / len(benchspecs))
    print(bold(f"| {name:11}                            {geomean_spec_score:5.2f} |"))

  print(bold("************************************************"))
  print(bold("|  SPEC CPU2026  | REFTIME  | RUNTIME  | SCORE |"))
  print(bold("************************************************"))
  if int_case:
    report_partial("SPECint2026", get_spec_int())
    print("------------------------------------------------")
  if fp_case:
    report_partial("SPECfp2026", get_spec_fp())
    print(bold("************************************************"))

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="report marks for SPEC CPU2026")
  parser.add_argument('--spec', default="all", type=str, help="Testcase FP/INT/ALL for SPEC2026 (fp, int, all)")
  parser.add_argument('--input', default="refrate", type=str, help='input of SPEC CPU2026 (refrate, train, test)')
  parser.add_argument('--run-tag', default="", type=str, help='tag for run directory')
  parser.add_argument('--verbose', '-v', default=False, action='store_true', help='verbose level')
  args = parser.parse_args()

  verbose = args.verbose
  run_tag = args.run_tag

  if args.spec == "all":
    fp_case = True
    int_case = True
  elif args.spec == "fp":
    fp_case = True
    int_case = False
  else:
    int_case = True
    fp_case = False

  report(args.input, fp_case, int_case, run_tag)
