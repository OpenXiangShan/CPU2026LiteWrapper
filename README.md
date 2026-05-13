# About

A lightweight, standalone Makefile-based wrapper for [SPEC CPU 2026](https://www.spec.org/cpu2026/) rate benchmarks.
It copies sources and data from a SPEC CPU 2026 installation and builds/runs them independently using plain Makefiles,
without requiring the SPEC harness at runtime (except for the `specdiff` validation tool).

Includes all 26 specrate benchmarks:

| SPECint 2026 rate (14) | SPECfp 2026 rate (12) |
|---|---|
| 706.stockfish_r | 709.cactus_r |
| 707.ntest_r | 722.palm_r |
| 708.sqlite_r | 731.astcenc_r |
| 710.omnetpp_r | 736.ocio_r |
| 714.cpython_r | 737.gmsh_r |
| 721.gcc_r | 748.flightdm_r |
| 723.llvm_r | 749.fotonik3d_r |
| 727.cppcheck_r | 765.roms_r |
| 729.abc_r | 766.femflow_r |
| 734.vpr_r | 767.nest_r |
| 735.gem5_r | 772.marian_r |
| 750.sealcrypto_r | 782.lbm_r |
| 753.ns3_r | |
| 777.zstd_r | |

# How to

- Set SPEC CPU 2026 path in env vars
```shell
export SPEC=/path/to/CPU2026
```

- Source shrc
```shell
cd $SPEC && source shrc
```

- Copy source
```shell
cd $SPEC_LITE
make copy_allr
```

- Copy data
```shell
make copy_data_all -j `nproc`
```

- Compile binaries
```shell
export ARCH=riscv64
export CROSS_COMPILE=riscv64-unknown-linux-gnu-
make build_allr -j `nproc`
```

- Collect result (optional)
```shell
bash scripts/collect.sh
```

- Run on localhost (optional)
```shell
make run-all-refrate # Don't use -j `nproc` here for single thread benchmarks
make report-int-refrate
make report-fp-refrate
```

You can also specify `VALIDATE=0` and `REPORT=0` to disable validation and report generation to speed up the running process,
this relaxes the need of `SPEC` env var at runtime:

```shell
make ARCH=riscv64 VALIDATE=0 REPORT=0 run-all-test
```

When running on real hardware, sometimes you may want to know the performance counters of the binaries, you can specify `PROFILER` argument to run the compiled binaries with a profiler such as `perf`:

```shell
make ARCH=riscv64 run-int-test PROFILER="perf stat -e cycles,instructions,branch-misses,cache-misses --append -o ../../perf.log"
```

When you need to compile different binaries with different architecture or flags, you can specify `TAG` argument to distinguish the compiled binaries, it will use `build$(TAG)` as the build folder name:

```shell
make ARCH=x86_64 build_allr -j `nproc`
make ARCH=x86_64 run-int-test
make ARCH=riscv64 TAG=-riscv64 build_allr -j `nproc`
make ARCH=riscv64 TAG=-riscv64 run-int-test
```

When you need to run multiple compiled binaries on shared storage (e.g. NFS) at the same time, you can specify `RUN_TAG` argument to distinguish the run folders, it will use `run$(RUN_TAG)` as the run folder name:

```shell
make ARCH=riscv64 RUN_TAG=-run1 run-int-test
make ARCH=riscv64 RUN_TAG=-run2 run-int-test
```

# Note for Fortran benchmarks

Some Fortran benchmarks (e.g. 765.roms_r) may require `ulimit -s unlimited` before running to avoid stack overflow, especially when compiled with LLVM's `flang-new`.

# Note for femflow

The 766.femflow_r benchmark has many large `inline` functions, but compiler may not inline them due to the cost model. We recommand adding `-DSPEC_INLINE_POLICY=LOOSE` to the CFLAGS when compiling femflow to make `inline` functions to be inlined more aggressively, which can significantly improve the performance in some cost models (e.g. GCC-16 with -O3 on x86-64). You can use `patch -p1 < patches/optional/766-femflow-inline.patch` to enable this.

# Note for lbm on AMD Zen 5 with GCC 16

We discovered 782.lbm_r may have 2x performance difference on AMD Zen 5 depending on PC alignment. When comparing the performance of AMD Zen 5 with other CPUs using GCC-16 with `-O3`. It's recommand to use `patch -p1 <patches/optional/782-lbm-zen5-prefetch-conflict.patch` to avoid the prefetch conflict issue which can cause significant performance degradation. For other compilers or different flags on Zen 5, the align issue may be different and need further manual tuning.

# Reference
- https://github.com/OpenXiangShan/CPU2006LiteWrapper
- https://github.com/OpenXiangShan/CPU2017LiteWrapper
