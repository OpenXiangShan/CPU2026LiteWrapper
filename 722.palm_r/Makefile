NAME = 722.palm_r
SRCS = $(addprefix src/,array_utilities.F90 \
	local_system.F90 \
	mod_kinds.F90 \
	basic_constants_and_equations_mod.F90 \
	chem_emis_biogenic_data_mod.F90 \
	chem_modules.F90 \
	cuda_fft_interfaces.F90 \
	data_output_binary_module.F90 \
	data_output_netcdf4_module.F90 \
	modules.F90 \
	pmc_general_mod.F90 \
	posix_interface_mod.F90 \
	random_function_mod.F90 \
	singleton_mod.F90 \
	surface_mod.F90 \
	time_to_string.F90 \
	wrd_write_string.F90 \
	chem_emis_pollen_data_mod.F90 \
	chem_isorropia_interface_mod.F90 \
	data_output_module.F90 \
	advec_s_pw.F90 \
	advec_s_up.F90 \
	advec_u_pw.F90 \
	advec_u_up.F90 \
	advec_v_pw.F90 \
	advec_v_up.F90 \
	advec_w_pw.F90 \
	advec_w_up.F90 \
	boundary_settings_mod.F90 \
	buoyancy.F90 \
	calc_mean_profile.F90 \
	chem_gasphase_mod.F90 \
	coriolis.F90 \
	cpulog_mod.F90 \
	data_log.F90 \
	general_utilities.F90 \
	global_min_max.F90 \
	gust_mod.F90 \
	init_advec.F90 \
	init_slope.F90 \
	init_vertical_profiles.F90 \
	mod_particle_attributes.F90 \
	model_1d_mod.F90 \
	palm_date_time_mod.F90 \
	progress_bar_mod.F90 \
	random_generator_parallel_mod.F90 \
	shared_memory_io_mod.F90 \
	subsidence_mod.F90 \
	temperton_fft_mod.F90 \
	timestep_scheme_steering.F90 \
	vdi_internal_controls.F90 \
	pmc_handle_communicator_mod.F90 \
	random_gauss.F90 \
	diffusion_s.F90 \
	diffusion_u.F90 \
	diffusion_v.F90 \
	diffusion_w.F90 \
	large_scale_forcing_nudging_mod.F90 \
	chem_emis_vsrc_mod.F90 \
	advec_s_bc.F90 \
	exchange_horiz_mod.F90 \
	local_tremain.F90 \
	local_tremain_ini.F90 \
	outflow_turbulence.F90 \
	print_1d.F90 \
	run_control.F90 \
	transpose_mod.F90 \
	user_module.F90 \
	disturb_heatflux.F90 \
	pmc_mpi_wrapper_mod.F90 \
	advec_ws.F90 \
	disturb_field.F90 \
	fastv8_coupler_mod.F90 \
	init_pt_anomaly.F90 \
	init_rankine.F90 \
	netcdf_data_input_mod.F90 \
	poismg_mod.F90 \
	poismg_noopt_mod.F90 \
	restart_data_mpi_io_mod.F90 \
	sor.F90 \
	surface_coupler_mod.F90 \
	fft_xy_mod.F90 \
	sm_poisfft_mod.F90 \
	tridia_solver_mod.F90 \
	user_data_output_mask.F90 \
	user_flight.F90 \
	user_init_3d_model.F90 \
	user_init_flight_mod.F90 \
	user_init_grid.F90 \
	user_lpm_advec.F90 \
	user_lpm_init.F90 \
	pmc_child_mod.F90 \
	pmc_parent_mod.F90 \
	chem_emis_generic_mod.F90 \
	chem_emis_nonstationary_mod.F90 \
	chem_emissions_mod.F90 \
	cut_cell_topography_mod.F90 \
	data_output_topo_and_surface_setup_mod.F90 \
	bulk_cloud_model_mod.F90 \
	turbulent_inflow_mod.F90 \
	spectra_mod.F90 \
	poisfft_mod.F90 \
	poisfft_sm_mod.F90 \
	chem_emis_domestic_mod.F90 \
	chem_emis_pt_source_mod.F90 \
	chem_emis_traffic_mod.F90 \
	chem_isorropia_mod.F90 \
	surface_data_handling.F90 \
	chem_wet_deposition_mod.F90 \
	compute_vpt.F90 \
	plant_canopy_model_mod.F90 \
	user_spectra.F90 \
	radiation_model_mod.F90 \
	salsa_mod.F90 \
	user_init_plant_canopy.F90 \
	biometeorology_mod.F90 \
	chem_emis_biogenic_mod.F90 \
	chem_emis_pollen_mod.F90 \
	chem_photolysis_mod.F90 \
	dcep_mod.F90 \
	urban_surface_mod.F90 \
	user_init_radiation.F90 \
	uv_radiation_model_mod.F90 \
	nesting_offl_mod.F90 \
	chemistry_model_mod.F90 \
	land_surface_model_mod.F90 \
	user_init_urban_surface.F90 \
	surface_layer_fluxes_mod.F90 \
	user_init_land_surface.F90 \
	virtual_measurement_mod.F90 \
	diagnostic_output_quantities_mod.F90 \
	dust_emission_and_transport_mod.F90 \
	indoor_model_mod.F90 \
	slurb_mod.F90 \
	pmc_interface_mod.F90 \
	check_for_restart.F90 \
	dynamics_mod.F90 \
	local_stop.F90 \
	message.F90 \
	ocean_mod.F90 \
	pmc_particle_interface.F90 \
	pres.F90 \
	synthetic_turbulence_generator_mod.F90 \
	topography_mod.F90 \
	wind_turbine_model_mod.F90 \
	init_grid.F90 \
	turbulence_closure_mod.F90 \
	data_output_particle_mod.F90 \
	init_pegrid.F90 \
	netcdf_interface_mod.F90 \
	lagrangian_particle_model_mod.F90 \
	check_open.F90 \
	close_file.F90 \
	data_output_mask.F90 \
	data_output_profiles.F90 \
	data_output_spectra.F90 \
	data_output_tseries.F90 \
	multi_agent_system_mod.F90 \
	virtual_flight_mod.F90 \
	data_output_flight.F90 \
	module_interface.F90 \
	average_3d_data.F90 \
	data_output_2d.F90 \
	data_output_3d.F90 \
	flow_statistics.F90 \
	header.F90 \
	init_masks.F90 \
	prognostic_equations.F90 \
	sum_up_3d_data.F90 \
	surface_data_output_mod.F90 \
	timestep.F90 \
	check_parameters.F90 \
	read_restart_data_mod.F90 \
	time_integration.F90 \
	time_integration_spinup.F90 \
	write_restart_data_mod.F90 \
	init_3d_model.F90 \
	parin.F90 \
	palm.F90)
SPEC_CFLAGS += 
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += 
SPECCPPFLAGS += -DSPEC_AUTO_SUPPRESS_THREADING
LD_FORTRAN = 1
.NOTPARALLEL:
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:
	rm -f src/array_utilities.fppized.f90 src/local_system.fppized.f90 src/mod_kinds.fppized.f90 src/basic_constants_and_equations_mod.fppized.f90 src/chem_emis_biogenic_data_mod.fppized.f90 src/chem_modules.fppized.f90 src/cuda_fft_interfaces.fppized.f90 src/data_output_binary_module.fppized.f90 src/data_output_netcdf4_module.fppized.f90 src/modules.fppized.f90 src/pmc_general_mod.fppized.f90 src/posix_interface_mod.fppized.f90 src/random_function_mod.fppized.f90 src/singleton_mod.fppized.f90 src/surface_mod.fppized.f90 src/time_to_string.fppized.f90 src/wrd_write_string.fppized.f90 src/chem_emis_pollen_data_mod.fppized.f90 src/chem_isorropia_interface_mod.fppized.f90 src/data_output_module.fppized.f90 src/advec_s_pw.fppized.f90 src/advec_s_up.fppized.f90 src/advec_u_pw.fppized.f90 src/advec_u_up.fppized.f90 src/advec_v_pw.fppized.f90 src/advec_v_up.fppized.f90 src/advec_w_pw.fppized.f90 src/advec_w_up.fppized.f90 src/boundary_settings_mod.fppized.f90 src/buoyancy.fppized.f90 src/calc_mean_profile.fppized.f90 src/chem_gasphase_mod.fppized.f90 src/coriolis.fppized.f90 src/cpulog_mod.fppized.f90 src/data_log.fppized.f90 src/general_utilities.fppized.f90 src/global_min_max.fppized.f90 src/gust_mod.fppized.f90 src/init_advec.fppized.f90 src/init_slope.fppized.f90 src/init_vertical_profiles.fppized.f90 src/mod_particle_attributes.fppized.f90 src/model_1d_mod.fppized.f90 src/palm_date_time_mod.fppized.f90 src/progress_bar_mod.fppized.f90 src/random_generator_parallel_mod.fppized.f90 src/shared_memory_io_mod.fppized.f90 src/subsidence_mod.fppized.f90 src/temperton_fft_mod.fppized.f90 src/timestep_scheme_steering.fppized.f90 src/vdi_internal_controls.fppized.f90 src/pmc_handle_communicator_mod.fppized.f90 src/random_gauss.fppized.f90 src/diffusion_s.fppized.f90 src/diffusion_u.fppized.f90 src/diffusion_v.fppized.f90 src/diffusion_w.fppized.f90 src/large_scale_forcing_nudging_mod.fppized.f90 src/chem_emis_vsrc_mod.fppized.f90 src/advec_s_bc.fppized.f90 src/exchange_horiz_mod.fppized.f90 src/local_tremain.fppized.f90 src/local_tremain_ini.fppized.f90 src/outflow_turbulence.fppized.f90 src/print_1d.fppized.f90 src/run_control.fppized.f90 src/transpose_mod.fppized.f90 src/user_module.fppized.f90 src/disturb_heatflux.fppized.f90 src/pmc_mpi_wrapper_mod.fppized.f90 src/advec_ws.fppized.f90 src/disturb_field.fppized.f90 src/fastv8_coupler_mod.fppized.f90 src/init_pt_anomaly.fppized.f90 src/init_rankine.fppized.f90 src/netcdf_data_input_mod.fppized.f90 src/poismg_mod.fppized.f90 src/poismg_noopt_mod.fppized.f90 src/restart_data_mpi_io_mod.fppized.f90 src/sor.fppized.f90 src/surface_coupler_mod.fppized.f90 src/fft_xy_mod.fppized.f90 src/sm_poisfft_mod.fppized.f90 src/tridia_solver_mod.fppized.f90 src/user_data_output_mask.fppized.f90 src/user_flight.fppized.f90 src/user_init_3d_model.fppized.f90 src/user_init_flight_mod.fppized.f90 src/user_init_grid.fppized.f90 src/user_lpm_advec.fppized.f90 src/user_lpm_init.fppized.f90 src/pmc_child_mod.fppized.f90 src/pmc_parent_mod.fppized.f90 src/chem_emis_generic_mod.fppized.f90 src/chem_emis_nonstationary_mod.fppized.f90 src/chem_emissions_mod.fppized.f90 src/cut_cell_topography_mod.fppized.f90 src/data_output_topo_and_surface_setup_mod.fppized.f90 src/bulk_cloud_model_mod.fppized.f90 src/turbulent_inflow_mod.fppized.f90 src/spectra_mod.fppized.f90 src/poisfft_mod.fppized.f90 src/poisfft_sm_mod.fppized.f90 src/chem_emis_domestic_mod.fppized.f90 src/chem_emis_pt_source_mod.fppized.f90 src/chem_emis_traffic_mod.fppized.f90 src/chem_isorropia_mod.fppized.f90 src/surface_data_handling.fppized.f90 src/chem_wet_deposition_mod.fppized.f90 src/compute_vpt.fppized.f90 src/plant_canopy_model_mod.fppized.f90 src/user_spectra.fppized.f90 src/radiation_model_mod.fppized.f90 src/salsa_mod.fppized.f90 src/user_init_plant_canopy.fppized.f90 src/biometeorology_mod.fppized.f90 src/chem_emis_biogenic_mod.fppized.f90 src/chem_emis_pollen_mod.fppized.f90 src/chem_photolysis_mod.fppized.f90 src/dcep_mod.fppized.f90 src/urban_surface_mod.fppized.f90 src/user_init_radiation.fppized.f90 src/uv_radiation_model_mod.fppized.f90 src/nesting_offl_mod.fppized.f90 src/chemistry_model_mod.fppized.f90 src/land_surface_model_mod.fppized.f90 src/user_init_urban_surface.fppized.f90 src/surface_layer_fluxes_mod.fppized.f90 src/user_init_land_surface.fppized.f90 src/virtual_measurement_mod.fppized.f90 src/diagnostic_output_quantities_mod.fppized.f90 src/dust_emission_and_transport_mod.fppized.f90 src/indoor_model_mod.fppized.f90 src/slurb_mod.fppized.f90 src/pmc_interface_mod.fppized.f90 src/check_for_restart.fppized.f90 src/dynamics_mod.fppized.f90 src/local_stop.fppized.f90 src/message.fppized.f90 src/ocean_mod.fppized.f90 src/pmc_particle_interface.fppized.f90 src/pres.fppized.f90 src/synthetic_turbulence_generator_mod.fppized.f90 src/topography_mod.fppized.f90 src/wind_turbine_model_mod.fppized.f90 src/init_grid.fppized.f90 src/turbulence_closure_mod.fppized.f90 src/data_output_particle_mod.fppized.f90 src/init_pegrid.fppized.f90 src/netcdf_interface_mod.fppized.f90 src/lagrangian_particle_model_mod.fppized.f90 src/check_open.fppized.f90 src/close_file.fppized.f90 src/data_output_mask.fppized.f90 src/data_output_profiles.fppized.f90 src/data_output_spectra.fppized.f90 src/data_output_tseries.fppized.f90 src/multi_agent_system_mod.fppized.f90 src/virtual_flight_mod.fppized.f90 src/data_output_flight.fppized.f90 src/module_interface.fppized.f90 src/average_3d_data.fppized.f90 src/data_output_2d.fppized.f90 src/data_output_3d.fppized.f90 src/flow_statistics.fppized.f90 src/header.fppized.f90 src/init_masks.fppized.f90 src/prognostic_equations.fppized.f90 src/sum_up_3d_data.fppized.f90 src/surface_data_output_mod.fppized.f90 src/timestep.fppized.f90 src/check_parameters.fppized.f90 src/read_restart_data_mod.fppized.f90 src/time_integration.fppized.f90 src/time_integration_spinup.fppized.f90 src/write_restart_data_mod.fppized.f90 src/init_3d_model.fppized.f90 src/parin.fppized.f90 src/palm.fppized.f90

refrate-cmp:
	@for f in RUN_CONTROL; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/refrate/output/$$f); \
	done
train-cmp:
	@for f in RUN_CONTROL; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/train/output/$$f); \
	done
test-cmp:
	@for f in RUN_CONTROL; do \
		$(call SPECDIFF, --abstol 0.0000004 --reltol 0.006, $(RUN_DIR)/$$f, data/test/output/$$f); \
	done
