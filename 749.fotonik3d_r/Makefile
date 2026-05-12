NAME = 749.fotonik3d_r
SRCS = $(addprefix src/,parameter.f90 \
	readline.f90 \
	timerRoutine.f90 \
	globalvar.F90 \
	MPI_dummy.F90 \
	power.F90 \
	communicate.F90 \
	huygens.F90 \
	update.F90 \
	material.F90 \
	PlaneSource.F90 \
	PEC.F90 \
	writeout.F90 \
	calcflops.F90 \
	mur.F90 \
	UPML.F90 \
	init.F90 \
	leapfrog.F90 \
	yeemain.F90)
SPEC_CFLAGS += -Isrc/. -DSPEC_AUTO_SUPPRESS_THREADING
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_FORTRAN = 1
.NOTPARALLEL:
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:
	rm -f src/globalvar.fppized.f90 src/MPI_dummy.fppized.f90 src/power.fppized.f90 src/communicate.fppized.f90 src/huygens.fppized.f90 src/update.fppized.f90 src/material.fppized.f90 src/PlaneSource.fppized.f90 src/PEC.fppized.f90 src/writeout.fppized.f90 src/calcflops.fppized.f90 src/mur.fppized.f90 src/UPML.fppized.f90 src/init.fppized.f90 src/leapfrog.fppized.f90 src/yeemain.fppized.f90

refrate-cmp:
	@for f in pscyee.out; do \
		$(call SPECDIFF, --obiwan --floatcompare --abstol 1e-26 --reltol 1e-7, $(RUN_DIR)/$$f, data/refrate/output/$$f); \
	done
train-cmp:
	@for f in pscyee.out; do \
		$(call SPECDIFF, --obiwan --floatcompare --abstol 1e-26 --reltol 1e-7, $(RUN_DIR)/$$f, data/train/output/$$f); \
	done
test-cmp:
	@for f in pscyee.out; do \
		$(call SPECDIFF, --obiwan --floatcompare --abstol 1e-26 --reltol 1e-7, $(RUN_DIR)/$$f, data/test/output/$$f); \
	done
