SPECFPRATE=709.cactus_r 722.palm_r 731.astcenc_r 736.ocio_r 737.gmsh_r 748.flightdm_r 749.fotonik3d_r 765.roms_r 766.femflow_r 767.nest_r 772.marian_r 782.lbm_r
SPECFPSPEED=
SPECINTRATE=706.stockfish_r 707.ntest_r 708.sqlite_r 710.omnetpp_r 714.cpython_r 721.gcc_r 723.llvm_r 727.cppcheck_r 729.abc_r 734.vpr_r 735.gem5_r 750.sealcrypto_r 753.ns3_r 777.zstd_r
SPECINTSPEED=

VALIDATE ?= 1
REPORT   ?= 1

ARCH ?= $(shell uname -m)
export ARCH

SPEC_LITE ?= $(CURDIR)
export SPEC_LITE

create_log_dir = @mkdir -p $*/logs
TIMESTAMP := $(shell date +%Y%m%d_%H%M%S)

copy_fp_%:
	@$(MAKE) -s -C $* copy-src
	@echo "Copying source files for FP target: $*"

copy_int_%:
	@$(MAKE) -s -C $* copy-src
	@echo "Copying source files for INT target: $*"

copy_data_fp_%:
	@$(MAKE) -s -C $* copy-data
	@echo "Copying data files for FP target: $*"

copy_data_int_%:
	@$(MAKE) -s -C $* copy-data
	@echo "Copying data files for INT target: $*"

build_fp_%:
	@$(call create_log_dir)
	@$(MAKE) -s -C $* >> $*/logs/build_fp_$*_$(TIMESTAMP).log 2>&1
	@echo "Building FP target: $*"

build_int_%:
	@$(call create_log_dir)
	@$(MAKE) -s -C $* SPECIFIC_FLAG=-ffp-contract=off  >> $*/logs/build_fp_$*_$(TIMESTAMP).log 2>&1
	@echo "Building INT target: $*"

clean_fp_%:
	@$(MAKE) -s -C $* clean
	@echo "Cleaning FP target: $*"

clean_int_%:
	@$(MAKE) -s -C $* clean
	@echo "Cleaning INT target: $*"

clean_src_fp_%:
	@$(MAKE) -s -C $* clean-src
	@echo "Cleaning source files for FP target: $*"

clean_src_int_%:
	@$(MAKE) -s -C $* clean-src
	@echo "Cleaning source files for INT target: $*"

clean_logs_fp_%:
	@$(MAKE) -s -C $* clean-logs
	@echo "Cleaning log files for FP target: $*"

clean_logs_int_%:
	@$(MAKE) -s -C $* clean-logs
	@echo "Cleaning log files for INT target: $*"

# Define the build and clean targets
build_fps: $(addprefix build_fp_, $(SPECFPSPEED))
build_ints: $(addprefix build_int_, $(SPECINTSPEED))
build_fpr: $(addprefix build_fp_, $(SPECFPRATE))
build_intr: $(addprefix build_int_, $(SPECINTRATE))
build_alls: build_ints build_fps
build_allr: build_intr build_fpr

clean_fps: $(addprefix clean_fp_, $(SPECFPSPEED))
clean_ints: $(addprefix clean_int_, $(SPECINTSPEED))
clean_fpr: $(addprefix clean_fp_, $(SPECFPRATE))
clean_intr: $(addprefix clean_int_, $(SPECINTRATE))
clean_alls: clean_ints clean_fps
clean_allr: clean_intr clean_fpr

clean_src_fpr: $(addprefix clean_src_fp_, $(SPECFPRATE))
clean_src_intr: $(addprefix clean_src_int_, $(SPECINTRATE))
clean_src_allr: clean_src_fpr clean_src_intr

copy_fpr: $(addprefix copy_fp_, $(SPECFPRATE))
copy_intr: $(addprefix copy_int_, $(SPECINTRATE))
copy_allr: copy_fpr copy_intr

copy_data_fp: $(addprefix copy_data_fp_, $(SPECFPRATE))
copy_data_int: $(addprefix copy_data_int_, $(SPECINTRATE))
copy_data_all: copy_data_fp copy_data_int

clean_logs_fpr: $(addprefix clean_logs_fp_, $(SPECFPRATE))
clean_logs_intr: $(addprefix clean_logs_int_, $(SPECINTRATE))
clean_logs_allr: clean_logs_fpr clean_logs_intr

# prototype: cmd_template(size)
define cmd_template
run-int-$(1): $(foreach t,$(SPECINTRATE),runeach-$t-$(1))
ifeq ($(REPORT),1)
	echo "\n\n\n"
	$(MAKE) report-int-$(1)
endif

validate-int-$(1):
	for t in $$(SPECINTRATE); do $(MAKE) -s -C $$$$t $(1)-cmp; done

run-fp-$(1): $(foreach t,$(SPECFPRATE),runeach-$t-$(1))
ifeq ($(REPORT),1)
	echo "\n\n\n"
	$(MAKE) report-fp-$(1)
endif

run-all-$(1): $(foreach t,$(SPECINTRATE) $(SPECFPRATE),runeach-$t-$(1))
ifeq ($(REPORT),1)
	echo "\n\n\n"
	$(MAKE) report-int-$(1)
	$(MAKE) report-fp-$(1)
endif

validate-fp-$(1):
	for t in $$(SPECFPRATE); do $(MAKE) -s -C $$$$t $(1)-cmp; done

runeach-%-$(1):
	echo "Running $(1) on $$*"
	@$(MAKE) -s -C $$* run TYPE=$(1) > $$*/logs/run-$(1).log
ifeq ($(VALIDATE),1)
	$(MAKE) validate-$$*-$(1)
endif

validate-%-$(1):
	@$(MAKE) -s -C $$* $(1)-cmp

report-int-$(1):
	@python scripts/report.py --input $(1) --spec int --run-tag "$(RUN_TAG)"

report-fp-$(1):
	@python scripts/report.py --input $(1) --spec fp --run-tag "$(RUN_TAG)"

endef

$(eval $(foreach size,test train refrate,$(call cmd_template,$(size))))
