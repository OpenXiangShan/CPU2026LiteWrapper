NAME = 727.cppcheck_r
SRCS = $(addprefix src/,cli/main.cpp \
	cli/cmdlineparser.cpp \
	cli/signalhandler.cpp \
	cli/singleexecutor.cpp \
	cli/cppcheckexecutor.cpp \
	cli/cppcheckexecutorseh.cpp \
	cli/cppcheckexecutorsig.cpp \
	cli/executor.cpp \
	cli/filelister.cpp \
	cli/processexecutor.cpp \
	cli/stacktrace.cpp \
	cli/threadexecutor.cpp \
	lib/addoninfo.cpp \
	lib/checkers.cpp \
	lib/checkersreport.cpp \
	lib/fwdanalysis.cpp \
	lib/keywords.cpp \
	lib/vfvalue.cpp \
	lib/analyzerinfo.cpp \
	lib/astutils.cpp \
	lib/check64bit.cpp \
	lib/checkassert.cpp \
	lib/checkautovariables.cpp \
	lib/checkbool.cpp \
	lib/checkboost.cpp \
	lib/checkbufferoverrun.cpp \
	lib/checkclass.cpp \
	lib/checkcondition.cpp \
	lib/check.cpp \
	lib/checkexceptionsafety.cpp \
	lib/checkfunctions.cpp \
	lib/checkinternal.cpp \
	lib/checkio.cpp \
	lib/checkleakautovar.cpp \
	lib/checkmemoryleak.cpp \
	lib/checknullpointer.cpp \
	lib/checkother.cpp \
	lib/checkpostfixoperator.cpp \
	lib/checksizeof.cpp \
	lib/checkstl.cpp \
	lib/checkstring.cpp \
	lib/checktype.cpp \
	lib/checkuninitvar.cpp \
	lib/checkunusedfunctions.cpp \
	lib/checkunusedvar.cpp \
	lib/checkvaarg.cpp \
	lib/clangimport.cpp \
	lib/color.cpp \
	lib/cppcheck.cpp \
	lib/ctu.cpp \
	lib/errorlogger.cpp \
	lib/errortypes.cpp \
	lib/forwardanalyzer.cpp \
	lib/importproject.cpp \
	lib/infer.cpp \
	lib/library.cpp \
	lib/mathlib.cpp \
	lib/pathanalysis.cpp \
	lib/path.cpp \
	lib/pathmatch.cpp \
	lib/platform.cpp \
	lib/preprocessor.cpp \
	lib/programmemory.cpp \
	lib/reverseanalyzer.cpp \
	lib/settings.cpp \
	lib/summaries.cpp \
	lib/suppressions.cpp \
	lib/symboldatabase.cpp \
	lib/templatesimplifier.cpp \
	lib/timer.cpp \
	lib/token.cpp \
	lib/tokenize.cpp \
	lib/tokenlist.cpp \
	lib/utils.cpp \
	lib/valueflow.cpp \
	lib/vf_array.cpp \
	lib/vf_arraybool.cpp \
	lib/vf_arrayelement.cpp \
	lib/vf_bailout.cpp \
	lib/vf_bitand.cpp \
	lib/vf_common.cpp \
	lib/vf_debug.cpp \
	lib/vf_enumvalue.cpp \
	lib/vf_functionreturn.cpp \
	lib/vf_globalconstvar.cpp \
	lib/vf_globalstaticvar.cpp \
	lib/vf_impossiblevalues.cpp \
	lib/vf_iteratorinfer.cpp \
	lib/vf_iterators.cpp \
	lib/vf_number.cpp \
	lib/vf_pointeralias.cpp \
	lib/vf_rightshift.cpp \
	lib/vf_sameexpressions.cpp \
	lib/vf_settokenvalue.cpp \
	lib/vf_string.cpp \
	lib/vf_symbolicinfer.cpp \
	lib/vf_unknownfunctionreturn.cpp \
	externals/simplecpp/simplecpp.cpp \
	externals/tinyxml2/tinyxml2.cpp)
SPEC_CFLAGS += -DSPEC_AUTO_SUPPRESS_THREADING -Isrc/externals -Isrc/externals/simplecpp -Isrc/externals/tinyxml2 -Isrc/externals/picojson -Isrc/cli -Isrc/lib -Isrc/spec_inline_control
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

TESTRUNNER_SRCS = $(filter-out src/cli/main.cpp,$(SRCS)) $(addprefix src/,test/options.cpp \
	test/fixture.cpp \
	test/helpers.cpp \
	test/testcheck.cpp \
	test/testcolor.cpp \
	test/testsettings.cpp \
	test/testsingleexecutor.cpp \
	test/test64bit.cpp \
	test/testanalyzerinformation.cpp \
	test/testassert.cpp \
	test/testastutils.cpp \
	test/testautovariables.cpp \
	test/testbool.cpp \
	test/testboost.cpp \
	test/testbufferoverrun.cpp \
	test/testcharvar.cpp \
	test/testclangimport.cpp \
	test/testclass.cpp \
	test/testcmdlineparser.cpp \
	test/testcondition.cpp \
	test/testconstructors.cpp \
	test/testcppcheck.cpp \
	test/testerrorlogger.cpp \
	test/testexceptionsafety.cpp \
	test/testfilelister.cpp \
	test/testfilesettings.cpp \
	test/testfunctions.cpp \
	test/testgarbage.cpp \
	test/testimportproject.cpp \
	test/testincompletestatement.cpp \
	test/testinternal.cpp \
	test/testio.cpp \
	test/testleakautovar.cpp \
	test/testlibrary.cpp \
	test/testmathlib.cpp \
	test/testmemleak.cpp \
	test/testnullpointer.cpp \
	test/testoptions.cpp \
	test/testother.cpp \
	test/testpath.cpp \
	test/testpathmatch.cpp \
	test/testplatform.cpp \
	test/testpostfixoperator.cpp \
	test/testpreprocessor.cpp \
	test/testprocessexecutor.cpp \
	test/testprogrammemory.cpp \
	test/testrunner.cpp \
	test/testsimplifytemplate.cpp \
	test/testsimplifytokens.cpp \
	test/testsimplifytypedef.cpp \
	test/testsimplifyusing.cpp \
	test/testsizeof.cpp \
	test/teststl.cpp \
	test/teststring.cpp \
	test/testsummaries.cpp \
	test/testsuppressions.cpp \
	test/testsymboldatabase.cpp \
	test/testthreadexecutor.cpp \
	test/testtimer.cpp \
	test/testtoken.cpp \
	test/testtokenize.cpp \
	test/testtokenlist.cpp \
	test/testtokenrange.cpp \
	test/testtype.cpp \
	test/testuninitvar.cpp \
	test/testunusedfunctions.cpp \
	test/testunusedprivfunc.cpp \
	test/testunusedvar.cpp \
	test/testutils.cpp \
	test/testvaarg.cpp \
	test/testvalueflow.cpp \
	test/testvarid.cpp)
TESTRUNNER_OBJS := $(patsubst %.F,%.fppized.o,$(TESTRUNNER_SRCS))
TESTRUNNER_OBJS := $(patsubst %.F90,%.fppized.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.f90,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.f,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.c,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.C,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.cpp,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.cc,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(patsubst %.cxx,%.o,$(TESTRUNNER_OBJS))
TESTRUNNER_OBJS := $(addprefix $(DST_DIR)/, $(TESTRUNNER_OBJS))
TESTRUNNER = $(abspath $(DST_DIR)/testrunner_r)

$(APP): $(TESTRUNNER)

$(TESTRUNNER): $(TESTRUNNER_OBJS)
	@echo + LD "->" $(notdir $@)
	@$(LD) -o $(abspath $@) $(TESTRUNNER_OBJS) $(LDFLAGS) $(JEMALLOC_LIBS)

refrate-cmp:
	@for f in 738_bogey.txt 738_report.txt 747_bogey.txt 747_report.txt 770_bogey.txt 770_report.txt cppcheck_r.738_bogey.out cppcheck_r.747_bogey.out cppcheck_r.770_bogey.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp:
	@for f in cppcheck_r.lcode_bogey.out cppcheck_r.mesh_bogey.out lcode_bogey.txt lcode_report.txt mesh_bogey.txt mesh_report.txt; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp:
	@for f in cppcheck_r.hello_bogey.out hello_bogey.txt testrunner_r.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
