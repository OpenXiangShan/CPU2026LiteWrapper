NAME = 731.astcenc_r
SRCS = $(addprefix src/,astcenc_averages_and_directions.cpp \
	astcenc_block_sizes.cpp \
	astcenc_color_quantize.cpp \
	astcenc_color_unquantize.cpp \
	astcenc_compress_symbolic.cpp \
	astcenc_compute_variance.cpp \
	astcenc_decompress_symbolic.cpp \
	astcenc_diagnostic_trace.cpp \
	astcenc_entry.cpp \
	astcenc_find_best_partitioning.cpp \
	astcenc_ideal_endpoints_and_weights.cpp \
	astcenc_image.cpp \
	astcenc_integer_sequence.cpp \
	astcenc_mathlib.cpp \
	astcenc_mathlib_softfloat.cpp \
	astcenc_partition_tables.cpp \
	astcenc_percentile_tables.cpp \
	astcenc_pick_best_endpoint_format.cpp \
	astcenc_quantization.cpp \
	astcenc_spec_main.cpp \
	astcenc_symbolic_physical.cpp \
	astcenc_weight_align.cpp \
	astcenc_weight_quant_xfer_tables.cpp \
	astcenccli_error_metrics.cpp \
	astcenccli_image.cpp \
	astcenccli_image_external.cpp \
	astcenccli_image_load_store.cpp \
	astcenccli_platform_dependents.cpp \
	astcenccli_toplevel.cpp \
	astcenccli_toplevel_help.cpp)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DSPEC_AUTO_SUPPRESS_THREADING -DSPECMAIN -Isrc/. -Isrc/ThirdParty -Isrc/spec_inline_control
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	@for f in astcenc_r.0.out astcenc_r.1.out astcenc_r.2.out; do \
		$(call SPECDIFF, --reltol 0.01, $(RUN_DIR)/$$f, data/refrate/output/$$f); \
	done
train-cmp:
	@for f in astcenc_r.0.out; do \
		$(call SPECDIFF, --reltol 0.01, $(RUN_DIR)/$$f, data/train/output/$$f); \
	done
test-cmp:
	@for f in astcenc_r.0.out; do \
		$(call SPECDIFF, --reltol 0.01, $(RUN_DIR)/$$f, data/test/output/$$f); \
	done
