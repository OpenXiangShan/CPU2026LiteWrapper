NAME = 777.zstd_r
SRCS = $(addprefix src/,zstd-1.5.6/programs/fileio.c \
	zstd-1.5.6/programs/fileio_asyncio.c \
	zstd-1.5.6/programs/util.c \
	zstd-1.5.6/programs/timefn.c \
	zstd-1.5.6/programs/zstdcli.c \
	zstd-1.5.6/programs/benchzstd.c \
	zstd-1.5.6/programs/datagen.c \
	zstd-1.5.6/programs/benchfn.c \
	zstd-1.5.6/programs/lorem.c \
	zstd-1.5.6/lib/compress/zstd_double_fast.c \
	zstd-1.5.6/lib/compress/zstd_fast.c \
	zstd-1.5.6/lib/compress/zstd_compress_sequences.c \
	zstd-1.5.6/lib/compress/zstd_ldm.c \
	zstd-1.5.6/lib/compress/hist.c \
	zstd-1.5.6/lib/compress/zstd_compress.c \
	zstd-1.5.6/lib/compress/zstd_compress_superblock.c \
	zstd-1.5.6/lib/compress/zstd_lazy.c \
	zstd-1.5.6/lib/compress/zstd_compress_literals.c \
	zstd-1.5.6/lib/compress/huf_compress.c \
	zstd-1.5.6/lib/compress/zstd_opt.c \
	zstd-1.5.6/lib/compress/fse_compress.c \
	zstd-1.5.6/lib/decompress/zstd_ddict.c \
	zstd-1.5.6/lib/decompress/huf_decompress.c \
	zstd-1.5.6/lib/decompress/zstd_decompress.c \
	zstd-1.5.6/lib/decompress/zstd_decompress_block.c \
	zstd-1.5.6/lib/common/entropy_common.c \
	zstd-1.5.6/lib/common/fse_decompress.c \
	zstd-1.5.6/lib/common/debug.c \
	zstd-1.5.6/lib/common/xxhash.c \
	zstd-1.5.6/lib/common/pool.c \
	zstd-1.5.6/lib/common/threading.c \
	zstd-1.5.6/lib/common/zstd_common.c \
	zstd-1.5.6/lib/common/error_private.c)
SPEC_CFLAGS += -DXXH_NAMESPACE=ZSTD_ -DZSTD_LEGACY_SUPPORT=0 -DZSTD_NODICT -DSTATIC_BMI2=0 -DDYNAMIC_BMI2=0 -DZSTD_NO_INTRINSICS=1 -DZSTD_DISABLE_ASM=1 -DZSTD_NOTRACE=1 -DZSTD_NO_TRACE=1 -Isrc/spec_inline_control -Isrc/lib -Isrc/lib/programs -Isrc/lib/common -Isrc/lib/compress -Isrc/lib/dictBuilder
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in zstd.b10_e10_verbose_i6_cld.tar.out zstd.b14_e14_verbose_i4_cld.tar.out zstd.b16_e16_verbose_i1_cld.tar.out zstd.b18_e18_verbose_i1_cld.tar.out zstd.b19_e19_verbose_i1_cld.tar.out zstd.b3_e3_verbose_i40_cld.tar.out zstd.b5_e5_verbose_i25_cld.tar.out zstd.b7_e7_verbose_i12_cld.tar.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp:
	@for f in zstd.b3_e12_verbose_i15.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp:
	@for f in zstd.b3_verbose_i1.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
