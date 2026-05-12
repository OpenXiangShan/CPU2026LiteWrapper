NAME = 734.vpr_r
SRCS = $(addprefix src/,vtr-vpr/vpr/src/main.cpp \
	vtr-vpr/vpr/src/analysis/timing_reports.cpp \
	vtr-vpr/vpr/src/base/CheckArch.cpp \
	vtr-vpr/vpr/src/base/CheckSetup.cpp \
	vtr-vpr/vpr/src/base/SetupGrid.cpp \
	vtr-vpr/vpr/src/base/SetupVPR.cpp \
	vtr-vpr/vpr/src/base/ShowSetup.cpp \
	vtr-vpr/vpr/src/base/atom_lookup.cpp \
	vtr-vpr/vpr/src/base/atom_netlist.cpp \
	vtr-vpr/vpr/src/base/atom_netlist_utils.cpp \
	vtr-vpr/vpr/src/base/check_netlist.cpp \
	vtr-vpr/vpr/src/base/clock_modeling.cpp \
	vtr-vpr/vpr/src/base/clustered_netlist.cpp \
	vtr-vpr/vpr/src/base/clustered_netlist_utils.cpp \
	vtr-vpr/vpr/src/base/constant_nets.cpp \
	vtr-vpr/vpr/src/base/constraints_load.cpp \
	vtr-vpr/vpr/src/base/echo_files.cpp \
	vtr-vpr/vpr/src/base/globals.cpp \
	vtr-vpr/vpr/src/base/logic_vec.cpp \
	vtr-vpr/vpr/src/base/netlist_walker.cpp \
	vtr-vpr/vpr/src/base/netlist_writer.cpp \
	vtr-vpr/vpr/src/base/partition.cpp \
	vtr-vpr/vpr/src/base/partition_region.cpp \
	vtr-vpr/vpr/src/base/place_and_route.cpp \
	vtr-vpr/vpr/src/base/read_activity.cpp \
	vtr-vpr/vpr/src/base/read_blif.cpp \
	vtr-vpr/vpr/src/base/read_circuit.cpp \
	vtr-vpr/vpr/src/base/read_netlist.cpp \
	vtr-vpr/vpr/src/base/read_options.cpp \
	vtr-vpr/vpr/src/base/read_place.cpp \
	vtr-vpr/vpr/src/base/read_route.cpp \
	vtr-vpr/vpr/src/base/region.cpp \
	vtr-vpr/vpr/src/base/setup_clocks.cpp \
	vtr-vpr/vpr/src/base/setup_noc.cpp \
	vtr-vpr/vpr/src/base/stats.cpp \
	vtr-vpr/vpr/src/base/vpr_api.cpp \
	vtr-vpr/vpr/src/base/vpr_constraints.cpp \
	vtr-vpr/vpr/src/base/vpr_constraints_reader.cpp \
	vtr-vpr/vpr/src/base/vpr_constraints_writer.cpp \
	vtr-vpr/vpr/src/base/vpr_signal_handler.cpp \
	vtr-vpr/vpr/src/base/vpr_tatum_error.cpp \
	vtr-vpr/vpr/src/base/vpr_types.cpp \
	vtr-vpr/vpr/src/noc/bfs_routing.cpp \
	vtr-vpr/vpr/src/noc/noc_link.cpp \
	vtr-vpr/vpr/src/noc/noc_router.cpp \
	vtr-vpr/vpr/src/noc/noc_routing_algorithm_creator.cpp \
	vtr-vpr/vpr/src/noc/noc_storage.cpp \
	vtr-vpr/vpr/src/noc/noc_traffic_flows.cpp \
	vtr-vpr/vpr/src/noc/read_xml_noc_traffic_flows_file.cpp \
	vtr-vpr/vpr/src/noc/xy_routing.cpp \
	vtr-vpr/vpr/src/pack/attraction_groups.cpp \
	vtr-vpr/vpr/src/pack/cluster.cpp \
	vtr-vpr/vpr/src/pack/cluster_feasibility_filter.cpp \
	vtr-vpr/vpr/src/pack/cluster_placement.cpp \
	vtr-vpr/vpr/src/pack/cluster_router.cpp \
	vtr-vpr/vpr/src/pack/cluster_util.cpp \
	vtr-vpr/vpr/src/pack/constraints_report.cpp \
	vtr-vpr/vpr/src/pack/lb_type_rr_graph.cpp \
	vtr-vpr/vpr/src/pack/output_clustering.cpp \
	vtr-vpr/vpr/src/pack/pack.cpp \
	vtr-vpr/vpr/src/pack/pack_report.cpp \
	vtr-vpr/vpr/src/pack/pb_type_graph.cpp \
	vtr-vpr/vpr/src/pack/pb_type_graph_annotations.cpp \
	vtr-vpr/vpr/src/pack/post_routing_pb_pin_fixup.cpp \
	vtr-vpr/vpr/src/pack/prepack.cpp \
	vtr-vpr/vpr/src/pack/re_cluster.cpp \
	vtr-vpr/vpr/src/pack/re_cluster_util.cpp \
	vtr-vpr/vpr/src/place/RL_agent_util.cpp \
	vtr-vpr/vpr/src/place/analytic_placer.cpp \
	vtr-vpr/vpr/src/place/centroid_move_generator.cpp \
	vtr-vpr/vpr/src/place/compressed_grid.cpp \
	vtr-vpr/vpr/src/place/critical_uniform_move_generator.cpp \
	vtr-vpr/vpr/src/place/cut_spreader.cpp \
	vtr-vpr/vpr/src/place/directed_moves_util.cpp \
	vtr-vpr/vpr/src/place/feasible_region_move_generator.cpp \
	vtr-vpr/vpr/src/place/grid_tile_lookup.cpp \
	vtr-vpr/vpr/src/place/initial_placement.cpp \
	vtr-vpr/vpr/src/place/manual_move_generator.cpp \
	vtr-vpr/vpr/src/place/median_move_generator.cpp \
	vtr-vpr/vpr/src/place/move_transactions.cpp \
	vtr-vpr/vpr/src/place/move_utils.cpp \
	vtr-vpr/vpr/src/place/place.cpp \
	vtr-vpr/vpr/src/place/place_checkpoint.cpp \
	vtr-vpr/vpr/src/place/place_constraints.cpp \
	vtr-vpr/vpr/src/place/place_delay_model.cpp \
	vtr-vpr/vpr/src/place/place_macro.cpp \
	vtr-vpr/vpr/src/place/place_timing_update.cpp \
	vtr-vpr/vpr/src/place/place_util.cpp \
	vtr-vpr/vpr/src/place/placer_breakpoint.cpp \
	vtr-vpr/vpr/src/place/placer_globals.cpp \
	vtr-vpr/vpr/src/place/simpleRL_move_generator.cpp \
	vtr-vpr/vpr/src/place/static_move_generator.cpp \
	vtr-vpr/vpr/src/place/timing_place.cpp \
	vtr-vpr/vpr/src/place/timing_place_lookup.cpp \
	vtr-vpr/vpr/src/place/uniform_move_generator.cpp \
	vtr-vpr/vpr/src/place/weighted_centroid_move_generator.cpp \
	vtr-vpr/vpr/src/place/weighted_median_move_generator.cpp \
	vtr-vpr/vpr/src/power/PowerSpicedComponent.cpp \
	vtr-vpr/vpr/src/power/power.cpp \
	vtr-vpr/vpr/src/power/power_callibrate.cpp \
	vtr-vpr/vpr/src/power/power_cmos_tech.cpp \
	vtr-vpr/vpr/src/power/power_components.cpp \
	vtr-vpr/vpr/src/power/power_lowlevel.cpp \
	vtr-vpr/vpr/src/power/power_sizing.cpp \
	vtr-vpr/vpr/src/power/power_util.cpp \
	vtr-vpr/vpr/src/route/annotate_routing.cpp \
	vtr-vpr/vpr/src/route/binary_heap.cpp \
	vtr-vpr/vpr/src/route/bucket.cpp \
	vtr-vpr/vpr/src/route/build_switchblocks.cpp \
	vtr-vpr/vpr/src/route/cb_metrics.cpp \
	vtr-vpr/vpr/src/route/channel_stats.cpp \
	vtr-vpr/vpr/src/route/check_route.cpp \
	vtr-vpr/vpr/src/route/clock_connection_builders.cpp \
	vtr-vpr/vpr/src/route/clock_network_builders.cpp \
	vtr-vpr/vpr/src/route/connection_based_routing.cpp \
	vtr-vpr/vpr/src/route/connection_router.cpp \
	vtr-vpr/vpr/src/route/edge_groups.cpp \
	vtr-vpr/vpr/src/route/heap_type.cpp \
	vtr-vpr/vpr/src/route/overuse_report.cpp \
	vtr-vpr/vpr/src/route/route_breadth_first.cpp \
	vtr-vpr/vpr/src/route/route_budgets.cpp \
	vtr-vpr/vpr/src/route/route_common.cpp \
	vtr-vpr/vpr/src/route/route_path_manager.cpp \
	vtr-vpr/vpr/src/route/route_profiling.cpp \
	vtr-vpr/vpr/src/route/route_timing.cpp \
	vtr-vpr/vpr/src/route/route_traceback.cpp \
	vtr-vpr/vpr/src/route/route_tree_timing.cpp \
	vtr-vpr/vpr/src/route/route_util.cpp \
	vtr-vpr/vpr/src/route/router_delay_profiling.cpp \
	vtr-vpr/vpr/src/route/router_lookahead.cpp \
	vtr-vpr/vpr/src/route/router_lookahead_cost_map.cpp \
	vtr-vpr/vpr/src/route/router_lookahead_extended_map.cpp \
	vtr-vpr/vpr/src/route/router_lookahead_map.cpp \
	vtr-vpr/vpr/src/route/router_lookahead_map_utils.cpp \
	vtr-vpr/vpr/src/route/router_lookahead_sampling.cpp \
	vtr-vpr/vpr/src/route/routing_predictor.cpp \
	vtr-vpr/vpr/src/route/rr_graph.cpp \
	vtr-vpr/vpr/src/route/rr_graph2.cpp \
	vtr-vpr/vpr/src/route/rr_graph_area.cpp \
	vtr-vpr/vpr/src/route/rr_graph_clock.cpp \
	vtr-vpr/vpr/src/route/rr_graph_indexed_data.cpp \
	vtr-vpr/vpr/src/route/rr_graph_sbox.cpp \
	vtr-vpr/vpr/src/route/rr_graph_timing_params.cpp \
	vtr-vpr/vpr/src/route/segment_stats.cpp \
	vtr-vpr/vpr/src/route/spatial_route_tree_lookup.cpp \
	vtr-vpr/vpr/src/timing/PreClusterTimingGraphResolver.cpp \
	vtr-vpr/vpr/src/timing/VprTimingGraphResolver.cpp \
	vtr-vpr/vpr/src/timing/concrete_timing_info.cpp \
	vtr-vpr/vpr/src/timing/net_delay.cpp \
	vtr-vpr/vpr/src/timing/read_sdc.cpp \
	vtr-vpr/vpr/src/timing/slack_evaluation.cpp \
	vtr-vpr/vpr/src/timing/timing_fail_error.cpp \
	vtr-vpr/vpr/src/timing/timing_graph_builder.cpp \
	vtr-vpr/vpr/src/timing/timing_util.cpp \
	vtr-vpr/vpr/src/util/hash.cpp \
	vtr-vpr/vpr/src/util/vpr_utils.cpp \
	vtr-vpr/libs/liblog/src/log.cpp \
	vtr-vpr/libs/libvtrutil/src/vpr_error.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_assert.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_color_map.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_digest.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_expr_eval.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_list.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_log.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_math.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_memory.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_path.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_random.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_rusage.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_time.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_token.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_util.cpp \
	vtr-vpr/libs/libvtrutil/src/vtr_version.cpp \
	specrand/specrand.cc \
	vtr-vpr/libs/libpugiutil/src/pugixml_loc.cpp \
	vtr-vpr/libs/libpugiutil/src/pugixml_util.cpp \
	vtr-vpr/libs/libarchfpga/src/arch_check.cpp \
	vtr-vpr/libs/libarchfpga/src/arch_error.cpp \
	vtr-vpr/libs/libarchfpga/src/arch_util.cpp \
	vtr-vpr/libs/libarchfpga/src/device_grid.cpp \
	vtr-vpr/libs/libarchfpga/src/echo_arch.cpp \
	vtr-vpr/libs/libarchfpga/src/histogram.cpp \
	vtr-vpr/libs/libarchfpga/src/parse_switchblocks.cpp \
	vtr-vpr/libs/libarchfpga/src/physical_types.cpp \
	vtr-vpr/libs/libarchfpga/src/physical_types_util.cpp \
	vtr-vpr/libs/libarchfpga/src/read_xml_arch_file.cpp \
	vtr-vpr/libs/libarchfpga/src/read_xml_util.cpp \
	vtr-vpr/libs/libarchfpga/src/write_models_bb.cpp \
	vtr-vpr/libs/librrgraph/src/base/check_rr_graph.cpp \
	vtr-vpr/libs/librrgraph/src/base/check_rr_graph_obj.cpp \
	vtr-vpr/libs/librrgraph/src/base/get_parallel_segs.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_graph_builder.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_graph_obj.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_graph_storage.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_graph_utils.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_graph_view.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_metadata.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_node.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_rc_data.cpp \
	vtr-vpr/libs/librrgraph/src/base/rr_spatial_lookup.cpp \
	vtr-vpr/libs/librrgraph/src/io/rr_graph_reader.cpp \
	vtr-vpr/libs/librrgraph/src/io/rr_graph_writer.cpp \
	vtr-vpr/libs/librrgraph/src/utils/alloc_and_load_rr_indexed_data.cpp \
	vtr-vpr/libs/librrgraph/src/utils/describe_rr_node.cpp \
	vtr-vpr/libs/EXTERNAL/libpugixml/src/pugixml.cpp \
	vtr-vpr/libs/EXTERNAL/libargparse/src/argparse.cpp \
	vtr-vpr/libs/EXTERNAL/libargparse/src/argparse_formatter.cpp \
	vtr-vpr/libs/EXTERNAL/libargparse/src/argparse_util.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdc_common.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdc_error.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdc_lexer.gen.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdc_parser.gen.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdcparse.cpp \
	vtr-vpr/libs/EXTERNAL/libsdcparse/src/sdc_lexer.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_common.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_error.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_lexer.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_pretty_print.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blifparse.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_lexer.gen.cpp \
	vtr-vpr/libs/EXTERNAL/libblifparse/src/blif_parser.gen.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/TimingConstraints.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/TimingGraph.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/TimingReporter.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/base/loop_detect.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/base/sta_util.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/base/validate_timing_graph_constraints.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/echo_writer.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/report/TimingPathCollector.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/report/graphviz_dot_writer.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/report/timing_path_tracing.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/tags/TimingTags.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/timing_paths.cpp \
	vtr-vpr/libs/EXTERNAL/libtatum/libtatum/tatum/util/tatum_assert.cpp \
	getdelim/getdelim.c)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -DNO_GRAPHICS -Isrc/vtr-vpr/vpr/src/analysis -Isrc/vtr-vpr/vpr/src/base -Isrc/vtr-vpr/vpr/src/base/gen -Isrc/vtr-vpr/vpr/src/noc -Isrc/vtr-vpr/vpr/src/pack -Isrc/vtr-vpr/vpr/src/place -Isrc/vtr-vpr/vpr/src/power -Isrc/vtr-vpr/vpr/src/route -Isrc/vtr-vpr/vpr/src/timing -Isrc/vtr-vpr/vpr/src/util -Isrc/vtr-vpr/libs/libvtrutil/src -Isrc/vtr-vpr/libs/liblog/src -Isrc/vtr-vpr/libs/libarchfpga/src -Isrc/vtr-vpr/libs/EXTERNAL/libpugixml/src -Isrc/vtr-vpr/libs/libpugiutil/src -Isrc/vtr-vpr/libs/EXTERNAL/libsdcparse/src -Isrc/vtr-vpr/libs/EXTERNAL/libsdcparse -Isrc/vtr-vpr/libs/EXTERNAL/libblifparse/src -Isrc/vtr-vpr/libs/EXTERNAL/libblifparse -Isrc/vtr-vpr/libs/EXTERNAL/libtatum/libtatum -Isrc/vtr-vpr/libs/EXTERNAL/libargparse/src -Isrc/vtr-vpr/libs/librrgraph/src/base -Isrc/vtr-vpr/libs/librrgraph/src/io/gen -Isrc/vtr-vpr/libs/librrgraph/src/io -Isrc/vtr-vpr/libs/librrgraph/src/utils -Isrc/getdelim -Isrc/specrand -Isrc/spec_include
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += -lm
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

# Build vpr_out_compare tool for validation
VPR_CMP_SRC = src/compare/vpr_out_compare.cpp
VPR_CMP_BIN = $(HOST_DIR)/vpr_out_compare
$(VPR_CMP_BIN): $(VPR_CMP_SRC)
	@mkdir -p $(HOST_DIR)
	$(HOST_CXX) -O2 -Isrc/spec_include -o $@ $<

PLACE_METRICS = swap_call swap_accepted swap_rejected
ROUTE_METRICS = num_rr_nodes num_rr_edges heap_pushes heap_pops critical_path_delay routed_wire_length

# Generate compare_*.out files by running vpr_out_compare on each log+metric pair
# Usage: $(call run_vpr_cmp,<size>,<blif_base>)
define run_vpr_cmp
	@for m in $(PLACE_METRICS); do \
		$(VPR_CMP_BIN) $$m data/$(1)/compare/$(2).place.log $(RUN_DIR)/$(2).place.log > $(RUN_DIR)/compare_$(2).place.log.$$m.out; \
	done
	@for m in $(ROUTE_METRICS); do \
		$(VPR_CMP_BIN) $$m data/$(1)/compare/$(2).route.log $(RUN_DIR)/$(2).route.log > $(RUN_DIR)/compare_$(2).route.log.$$m.out; \
	done
endef

refrate-cmp: $(VPR_CMP_BIN)
	$(call run_vpr_cmp,refrate,JPEG_stratixiv_arch_timing.blif)
	$(call run_vpr_cmp,refrate,smithwaterman_stratixiv_arch_timing.blif)
	@for f in compare_JPEG_stratixiv_arch_timing.blif.place.log.swap_accepted.out compare_JPEG_stratixiv_arch_timing.blif.place.log.swap_call.out compare_JPEG_stratixiv_arch_timing.blif.place.log.swap_rejected.out compare_JPEG_stratixiv_arch_timing.blif.route.log.critical_path_delay.out compare_JPEG_stratixiv_arch_timing.blif.route.log.heap_pops.out compare_JPEG_stratixiv_arch_timing.blif.route.log.heap_pushes.out compare_JPEG_stratixiv_arch_timing.blif.route.log.num_rr_edges.out compare_JPEG_stratixiv_arch_timing.blif.route.log.num_rr_nodes.out compare_JPEG_stratixiv_arch_timing.blif.route.log.routed_wire_length.out compare_smithwaterman_stratixiv_arch_timing.blif.place.log.swap_accepted.out compare_smithwaterman_stratixiv_arch_timing.blif.place.log.swap_call.out compare_smithwaterman_stratixiv_arch_timing.blif.place.log.swap_rejected.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.critical_path_delay.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.heap_pops.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.heap_pushes.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.num_rr_edges.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.num_rr_nodes.out compare_smithwaterman_stratixiv_arch_timing.blif.route.log.routed_wire_length.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/refrate/output/$$f; \
	done
train-cmp: $(VPR_CMP_BIN)
	$(call run_vpr_cmp,train,sudoku_check_stratixiv_arch_timing.blif)
	@for f in compare_sudoku_check_stratixiv_arch_timing.blif.place.log.swap_accepted.out compare_sudoku_check_stratixiv_arch_timing.blif.place.log.swap_call.out compare_sudoku_check_stratixiv_arch_timing.blif.place.log.swap_rejected.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.critical_path_delay.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.heap_pops.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.heap_pushes.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.num_rr_edges.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.num_rr_nodes.out compare_sudoku_check_stratixiv_arch_timing.blif.route.log.routed_wire_length.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/train/output/$$f; \
	done
test-cmp: $(VPR_CMP_BIN)
	$(call run_vpr_cmp,test,murax_stratixiv_arch_timing.blif)
	@for f in compare_murax_stratixiv_arch_timing.blif.place.log.swap_accepted.out compare_murax_stratixiv_arch_timing.blif.place.log.swap_call.out compare_murax_stratixiv_arch_timing.blif.place.log.swap_rejected.out compare_murax_stratixiv_arch_timing.blif.route.log.critical_path_delay.out compare_murax_stratixiv_arch_timing.blif.route.log.heap_pops.out compare_murax_stratixiv_arch_timing.blif.route.log.heap_pushes.out compare_murax_stratixiv_arch_timing.blif.route.log.num_rr_edges.out compare_murax_stratixiv_arch_timing.blif.route.log.num_rr_nodes.out compare_murax_stratixiv_arch_timing.blif.route.log.routed_wire_length.out; do \
		$(DIFF) $(RUN_DIR)/$$f data/test/output/$$f; \
	done
