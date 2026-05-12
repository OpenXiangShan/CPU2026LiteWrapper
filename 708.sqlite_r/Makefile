NAME = 708.sqlite_r
SRCS = $(addprefix src/,sqlite3.c speedtest1.c)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DSQLITE_DISABLE_INTRINSIC -DSQLITE_OMIT_LOAD_EXTENSION -DSQLITE_THREADSAFE=0 -DSQLITE_ENABLE_RTREE -DSQLITE_OMIT_DEPRECATED -DSQLITE_OMIT_TRACE -DSQLITE_OMIT_RANDOMNESS -DSQLITE_OMIT_WAL -Isrc/spec_inline_control
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += -lm
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in sqlite_r.cte.out sqlite_r.fp.out sqlite_r.main.out; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/refrate/output/$$f); \
	done
train-cmp:
	@for f in sqlite_r.cte.out sqlite_r.main.out; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/train/output/$$f); \
	done
test-cmp:
	@for f in sqlite_r.main.out; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/test/output/$$f); \
	done
