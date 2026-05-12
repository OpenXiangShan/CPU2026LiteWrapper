NAME = 750.sealcrypto_r
SRCS = $(addprefix src/,specrand/specrand.cc \
	seal/util/blake2b.c \
	seal/util/blake2xb.c \
	seal/util/fips202.c \
	seal/batchencoder.cpp \
	seal/ciphertext.cpp \
	seal/ckks.cpp \
	seal/context.cpp \
	seal/decryptor.cpp \
	seal/encryptionparams.cpp \
	seal/encryptor.cpp \
	seal/evaluator.cpp \
	seal/keygenerator.cpp \
	seal/kswitchkeys.cpp \
	seal/memorymanager.cpp \
	seal/modulus.cpp \
	seal/plaintext.cpp \
	seal/randomgen.cpp \
	seal/serialization.cpp \
	seal/valcheck.cpp \
	seal/util/clipnormal.cpp \
	seal/util/common.cpp \
	seal/util/croots.cpp \
	seal/util/globals.cpp \
	seal/util/galois.cpp \
	seal/util/hash.cpp \
	seal/util/iterator.cpp \
	seal/util/mempool.cpp \
	seal/util/numth.cpp \
	seal/util/polyarithsmallmod.cpp \
	seal/util/rlwe.cpp \
	seal/util/rns.cpp \
	seal/util/scalingvariant.cpp \
	seal/util/ntt.cpp \
	seal/util/streambuf.cpp \
	seal/util/uintarith.cpp \
	seal/util/uintarithmod.cpp \
	seal/util/uintarithsmallmod.cpp \
	seal/util/uintcore.cpp \
	seal/util/ztools.cpp \
	secure-query/main.cpp \
	secure-query/sqclient.cpp \
	secure-query/sqserver.cpp)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DSPEC_AUTO_SUPPRESS_THREADING -Isrc/. -Isrc/specrand -Isrc/specrand-distributions -Isrc/seal -Isrc/seal/util -Isrc/secure-query -Isrc/secure-query/include
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in homoencrypt.refrate_ecuador_province_capitals_refrate.csv_Galapagos.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp:
	@for f in homoencrypt.train_australia_state_capitals_train.csv_Victoria.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp:
	@for f in homoencrypt.test_country_capital_test.csv_Ecuador.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
