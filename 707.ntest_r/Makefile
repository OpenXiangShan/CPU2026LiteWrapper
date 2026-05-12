NAME = 707.ntest_r
SRCS = $(addprefix src/,BitBoard.cpp \
	BitBoardTest.cpp \
	Cache.cpp \
	CalcParams.cpp \
	EvalTest.cpp \
	Evaluator.cpp \
	FastFlip.cpp \
	HeightInfo.cpp \
	MPCStats.cpp \
	MVK.cpp \
	Moves.cpp \
	NodeStats.cpp \
	OsObjects.cpp \
	Patterns.cpp \
	Player.cpp \
	PlayerComputer.cpp \
	Pos2.cpp \
	Pos2Test.cpp \
	QPosition.cpp \
	QPositionTest.cpp \
	Search.cpp \
	SearchParams.cpp \
	SearchTest.cpp \
	SpeedTest.cpp \
	Stable.cpp \
	bitExtractTest.cpp \
	endgameSearch.cpp \
	endgameSearchTest.cpp \
	flips.cpp \
	flipsTest.cpp \
	hash.cpp \
	hashTest.cpp \
	lastFlipCountGenerator.cpp \
	n64.cpp \
	odkTest.cpp \
	options.cpp \
	port.cpp \
	solve.cpp \
	solveTest.cpp \
	speed_test.cpp \
	test.cpp \
	utils.cpp \
	utilsTest.cpp \
	specrand/specrand.cc)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DSPEC_AUTO_SUPPRESS_THREADING -Isrc/specrand
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in ntest.Othello.154.20.16.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp:
	@for f in ntest.Othello.60e4.19.19.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp:
	@for f in ntest.OneGame.10.6.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
