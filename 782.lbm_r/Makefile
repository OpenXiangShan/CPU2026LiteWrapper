NAME = 782.lbm_r
SRCS = $(addprefix src/,lbm.c main.c)
SPEC_CFLAGS += -DSPEC_AUTO_SUPPRESS_THREADING -DSPEC_RATE
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += -lm
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in lbm.out; do \
		$(call SPECDIFF, --abstol 0.0000001, $(RUN_DIR)/$$f, data/refrate/output/$$f); \
	done
train-cmp:
	@for f in lbm.out; do \
		$(call SPECDIFF, --abstol 0.0000001, $(RUN_DIR)/$$f, data/train/output/$$f); \
	done
test-cmp:
	@for f in lbm.out; do \
		$(call SPECDIFF, --abstol 0.0000001, $(RUN_DIR)/$$f, data/test/output/$$f); \
	done
