NAME = 706.stockfish_r
SRCS = $(addprefix src/,benchmark.cpp \
	bitbase.cpp \
	bitboard.cpp \
	endgame.cpp \
	evaluate.cpp \
	main.cpp \
	material.cpp \
	misc.cpp \
	movegen.cpp \
	movepick.cpp \
	pawns.cpp \
	position.cpp \
	psqt.cpp \
	search.cpp \
	thread.cpp \
	timeman.cpp \
	tt.cpp \
	uci.cpp \
	ucioption.cpp \
	nnue/evaluate_nnue.cpp \
	nnue/features/half_ka_v2_hm.cpp)
SPEC_CFLAGS += 
SPEC_CXXFLAGS += -DIS_64BIT -DUSE_MAGIC_MSB -DSPEC_AUTO_SUPPRESS_THREADING -Isrc/spec_restrict
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in stockfish_spec_ref_pos_1to6_classical.out stockfish_spec_ref_pos_1to6_nnue.out stockfish_spec_ref_pos_7to11_nnue.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp:
	@for f in stockfish_spec_train_classical.out stockfish_spec_train_nnue.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp:
	@for f in stockfish_spec_test_classical.out stockfish_spec_test_nnue.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
