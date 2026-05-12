#!/usr/bin/perl
# Extract source file lists and flags from SPEC CPU2026 .pm files
# Usage: perl extract_sources.pl <benchmark_dir> [flags]
# Default mode: outputs one source file per line (or exe:source for multi-exe)
# flags mode: outputs FLAG_NAME=value lines

use warnings;
use Config;

my $benchdir = $ARGV[0] or die "Usage: $0 <benchmark_pm_dir> [flags]\n";
my $mode = $ARGV[1] || 'sources';
my $pm_path = "$benchdir/Spec/object.pm";

open(my $fh, '<', $pm_path) or die "Cannot open $pm_path: $!\n";
my $content = do { local $/; <$fh> };
close($fh);

# Evaluate in a package that allows undeclared globals
{
    package SpecEval;
    no strict;
    no warnings;
    use Config;

    # Provide stubs for common subs referenced in .pm files
    sub invoke { return () }
    sub read_file { return '' }
    sub filename_safe_string { return $_[0] }
    sub jp { return join('/', @_) }

    eval $content;
    if ($@) {
        warn "Eval warning: $@\n";
    }

    if ($mode eq 'flags') {
        print "BENCH_FLAGS=$bench_flags\n" if defined $bench_flags;
        print "BENCH_CXXFLAGS=$bench_cxxflags\n" if defined $bench_cxxflags;
        print "BENCH_FFLAGS=$bench_fflags\n" if defined $bench_fflags;
        print "BENCH_FPPFLAGS=$bench_fppflags\n" if defined $bench_fppflags;
        print "BENCH_LDFLAGS=$bench_ldflags\n" if defined $bench_ldflags;
        print "NEED_MATH=$need_math\n" if defined $need_math;
        print "BENCHLANG=$benchlang\n" if defined $benchlang;
        print "EXENAME=$exename\n" if defined $exename;
        if (@base_exe) {
            print "BASE_EXE=" . join(' ', @base_exe) . "\n";
        }
    } else {
        if (@sources) {
            for my $src (@sources) {
                print "$src\n";
            }
        } elsif (%sources) {
            for my $exe (sort keys %sources) {
                for my $src (@{$sources{$exe}}) {
                    print "$exe:$src\n";
                }
            }
        }
    }
}
