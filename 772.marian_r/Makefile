NAME = 772.marian_r
SRCS = $(addprefix src/,marian/command/marian_decoder.cpp \
	marian/common/aliases.cpp \
	marian/common/binary.cpp \
	marian/common/cli_helper.cpp \
	marian/common/cli_wrapper.cpp \
	marian/common/config.cpp \
	marian/common/config_parser.cpp \
	marian/common/config_validator.cpp \
	marian/common/fastopt.cpp \
	marian/common/file_stream.cpp \
	marian/common/file_utils.cpp \
	marian/common/filesystem.cpp \
	marian/common/io.cpp \
	marian/common/logging.cpp \
	marian/common/options.cpp \
	marian/common/signal_handling.cpp \
	marian/common/types.cpp \
	marian/common/utils.cpp \
	marian/common/version.cpp \
	marian/data/alignment.cpp \
	marian/data/corpus.cpp \
	marian/data/corpus_base.cpp \
	marian/data/corpus_nbest.cpp \
	marian/data/default_vocab.cpp \
	marian/data/factored_vocab.cpp \
	marian/data/sentencepiece_vocab.cpp \
	marian/data/shortlist.cpp \
	marian/data/text_input.cpp \
	marian/data/vocab.cpp \
	marian/embedder/vector_collector.cpp \
	marian/graph/expression_graph.cpp \
	marian/graph/expression_operators.cpp \
	marian/graph/node.cpp \
	marian/graph/node_initializers.cpp \
	marian/graph/node_operators.cpp \
	marian/layers/convolution.cpp \
	marian/layers/embedding.cpp \
	marian/layers/generic.cpp \
	marian/layers/logits.cpp \
	marian/layers/loss.cpp \
	marian/layers/lsh.cpp \
	marian/layers/output.cpp \
	marian/layers/weight.cpp \
	marian/microsoft/quicksand.cpp \
	marian/microsoft/shortlist/utils/Converter.cpp \
	marian/microsoft/shortlist/utils/ParameterTree.cpp \
	marian/microsoft/shortlist/utils/StringUtils.cpp \
	marian/models/costs.cpp \
	marian/models/encoder_decoder.cpp \
	marian/models/model_factory.cpp \
	marian/models/transformer_stub.cpp \
	marian/rescorer/score_collector.cpp \
	marian/rnn/attention.cpp \
	marian/rnn/cells.cpp \
	marian/tensors/backend.cpp \
	marian/tensors/cpu/device.cpp \
	marian/tensors/cpu/integer_common.cpp \
	marian/tensors/cpu/prod.cpp \
	marian/tensors/cpu/tensor_operators.cpp \
	marian/tensors/cpu/topk.cpp \
	marian/tensors/rand.cpp \
	marian/tensors/tensor.cpp \
	marian/translator/beam_search.cpp \
	marian/translator/helpers.cpp \
	marian/translator/history.cpp \
	marian/translator/nth_element.cpp \
	marian/translator/output_collector.cpp \
	marian/translator/output_printer.cpp \
	marian/translator/scorers.cpp \
	marian/3rd_party/cnpy/cnpy.cpp \
	marian/3rd_party/pathie-cpp/src/entry_iterator.cpp \
	marian/3rd_party/pathie-cpp/src/errors.cpp \
	marian/3rd_party/pathie-cpp/src/path.cpp \
	marian/3rd_party/pathie-cpp/src/pathie.cpp \
	marian/3rd_party/pathie-cpp/src/pathie_ifstream.cpp \
	marian/3rd_party/pathie-cpp/src/pathie_ofstream.cpp \
	marian/3rd_party/pathie-cpp/src/temp.cpp \
	marian/3rd_party/phf/phf.cc \
	marian/3rd_party/sentencepiece/src/bpe_model.cc \
	marian/3rd_party/sentencepiece/src/builtin_pb/sentencepiece.pb.cc \
	marian/3rd_party/sentencepiece/src/builtin_pb/sentencepiece_model.pb.cc \
	marian/3rd_party/sentencepiece/src/case_encoder.cc \
	marian/3rd_party/sentencepiece/src/char_model.cc \
	marian/3rd_party/sentencepiece/src/error.cc \
	marian/3rd_party/sentencepiece/src/filesystem.cc \
	marian/3rd_party/sentencepiece/src/init.cc \
	marian/3rd_party/sentencepiece/src/model_factory.cc \
	marian/3rd_party/sentencepiece/src/model_interface.cc \
	marian/3rd_party/sentencepiece/src/normalizer.cc \
	marian/3rd_party/sentencepiece/src/sentencepiece_processor.cc \
	marian/3rd_party/sentencepiece/src/unigram_model.cc \
	marian/3rd_party/sentencepiece/src/util.cc \
	marian/3rd_party/sentencepiece/src/word_model.cc \
	marian/3rd_party/sentencepiece/third_party/absl/flags/flag.cc \
	marian/3rd_party/sentencepiece/third_party/absl/strings/string_view.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/arena.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/arenastring.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/bytestream.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/coded_stream.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/common.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/extension_set.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/generated_message_table_driven_lite.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/generated_message_util.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/implicit_weak_message.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/int128.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/io_win32.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/message_lite.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/repeated_field.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/status.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/statusor.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/stringpiece.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/stringprintf.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/structurally_valid.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/strutil.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/time.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/wire_format_lite.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/zero_copy_stream.cc \
	marian/3rd_party/sentencepiece/third_party/protobuf-lite/zero_copy_stream_impl_lite.cc \
	marian/3rd_party/yaml-cpp/binary_renamed.cpp \
	marian/3rd_party/yaml-cpp/convert.cpp \
	marian/3rd_party/yaml-cpp/directives.cpp \
	marian/3rd_party/yaml-cpp/emit.cpp \
	marian/3rd_party/yaml-cpp/emitfromevents.cpp \
	marian/3rd_party/yaml-cpp/emitter.cpp \
	marian/3rd_party/yaml-cpp/emitterstate.cpp \
	marian/3rd_party/yaml-cpp/emitterutils.cpp \
	marian/3rd_party/yaml-cpp/exceptions.cpp \
	marian/3rd_party/yaml-cpp/exp.cpp \
	marian/3rd_party/yaml-cpp/memory.cpp \
	marian/3rd_party/yaml-cpp/node_data.cpp \
	marian/3rd_party/yaml-cpp/nodebuilder.cpp \
	marian/3rd_party/yaml-cpp/nodeevents.cpp \
	marian/3rd_party/yaml-cpp/null.cpp \
	marian/3rd_party/yaml-cpp/ostream_wrapper.cpp \
	marian/3rd_party/yaml-cpp/parse.cpp \
	marian/3rd_party/yaml-cpp/parser.cpp \
	marian/3rd_party/yaml-cpp/regex_yaml.cpp \
	marian/3rd_party/yaml-cpp/scanner.cpp \
	marian/3rd_party/yaml-cpp/scanscalar.cpp \
	marian/3rd_party/yaml-cpp/scantag.cpp \
	marian/3rd_party/yaml-cpp/scantoken.cpp \
	marian/3rd_party/yaml-cpp/simplekey.cpp \
	marian/3rd_party/yaml-cpp/singledocparser.cpp \
	marian/3rd_party/yaml-cpp/stream.cpp \
	marian/3rd_party/yaml-cpp/tag.cpp \
	marian/3rd_party/yaml-cpp/yaml-node.cpp \
	specrand/specrand.cc)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DSPEC_AUTO_SUPPRESS_THREADING -Isrc/marian/3rd_party/sentencepiece -Isrc/marian/3rd_party/sentencepiece/src/builtin_pb -Isrc/marian/3rd_party/sentencepiece/third_party/protobuf-lite -Isrc/marian/3rd_party -Isrc/marian/3rd_party/intgemm -Isrc/marian/data -Isrc/marian/common -Isrc/marian/tensors -Isrc/marian/graph -Isrc/marian -Isrc/specrand -D_USE_INTERNAL_STRING_VIEW -DCOMPILE_CPU=1 -DUSE_SENTENCEPIECE -DPHF_HAVE_COMPUTED_GOTOS=0
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

# Build text_compare tool for validation
TEXT_CMP_SRC = src/compare/text_compare.cpp
TEXT_CMP_BIN = $(HOST_DIR)/text_compare
$(TEXT_CMP_BIN): $(TEXT_CMP_SRC)
	@mkdir -p $(HOST_DIR)
	$(HOST_CXX) -O2 -o $@ $<

# Generate compare_<name>.out files by running text_compare
# Usage: $(call run_text_cmp,<size>,<name>)
# Compares <run_dir>/<name> against data/<size>/compare/<name>
define run_text_cmp
	$(TEXT_CMP_BIN) $(RUN_DIR)/$(2) data/$(1)/compare/$(2) > $(RUN_DIR)/compare_$(2).out
endef

refrate-cmp: $(TEXT_CMP_BIN)
	$(call run_text_cmp,refrate,EuroPat-spec.out)
	$(call run_text_cmp,refrate,TildeMODEL-spec.out)
	@for f in compare_EuroPat-spec.out.out compare_TildeMODEL-spec.out.out; do \
		$(call SPECDIFF,--abstol 0.01,$(RUN_DIR)/$$f,data/refrate/output/$$f); \
	done
train-cmp: $(TEXT_CMP_BIN)
	$(call run_text_cmp,train,technology_and_courage.out)
	@for f in compare_technology_and_courage.out.out; do \
		$(call SPECDIFF,--abstol 0.01,$(RUN_DIR)/$$f,data/train/output/$$f); \
	done
test-cmp: $(TEXT_CMP_BIN)
	$(call run_text_cmp,test,TildeMODEL-test.out)
	@for f in compare_TildeMODEL-test.out.out; do \
		$(call SPECDIFF,--abstol 0.01,$(RUN_DIR)/$$f,data/test/output/$$f); \
	done
