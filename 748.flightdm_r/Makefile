NAME = 748.flightdm_r
SRCS = $(addprefix src/,JSB-FlightSim/src/FGFDMExec.cpp \
	JSB-FlightSim/src/FGJSBBase.cpp \
	JSB-FlightSim/src/GeographicLib/Geodesic.cpp \
	JSB-FlightSim/src/GeographicLib/GeodesicLine.cpp \
	JSB-FlightSim/src/GeographicLib/Math.cpp \
	JSB-FlightSim/src/JSBSim.cpp \
	JSB-FlightSim/src/initialization/FGInitialCondition.cpp \
	JSB-FlightSim/src/initialization/FGLinearization.cpp \
	JSB-FlightSim/src/initialization/FGTrim.cpp \
	JSB-FlightSim/src/initialization/FGTrimAxis.cpp \
	JSB-FlightSim/src/input_output/FGGroundCallback.cpp \
	JSB-FlightSim/src/input_output/FGInputType.cpp \
	JSB-FlightSim/src/input_output/FGModelLoader.cpp \
	JSB-FlightSim/src/input_output/FGOutputFile.cpp \
	JSB-FlightSim/src/input_output/FGOutputTextFile.cpp \
	JSB-FlightSim/src/input_output/FGOutputType.cpp \
	JSB-FlightSim/src/input_output/FGPropertyManager.cpp \
	JSB-FlightSim/src/input_output/FGPropertyReader.cpp \
	JSB-FlightSim/src/input_output/FGScript.cpp \
	JSB-FlightSim/src/input_output/FGXMLElement.cpp \
	JSB-FlightSim/src/input_output/FGXMLFileRead.cpp \
	JSB-FlightSim/src/input_output/FGXMLParse.cpp \
	JSB-FlightSim/src/input_output/string_utilities.cpp \
	JSB-FlightSim/src/math/FGColumnVector3.cpp \
	JSB-FlightSim/src/math/FGCondition.cpp \
	JSB-FlightSim/src/math/FGFunction.cpp \
	JSB-FlightSim/src/math/FGLocation.cpp \
	JSB-FlightSim/src/math/FGMatrix33.cpp \
	JSB-FlightSim/src/math/FGModelFunctions.cpp \
	JSB-FlightSim/src/math/FGNelderMead.cpp \
	JSB-FlightSim/src/math/FGPropertyValue.cpp \
	JSB-FlightSim/src/math/FGQuaternion.cpp \
	JSB-FlightSim/src/math/FGRealValue.cpp \
	JSB-FlightSim/src/math/FGRungeKutta.cpp \
	JSB-FlightSim/src/math/FGStateSpace.cpp \
	JSB-FlightSim/src/math/FGTable.cpp \
	JSB-FlightSim/src/math/FGTemplateFunc.cpp \
	JSB-FlightSim/src/models/FGAccelerations.cpp \
	JSB-FlightSim/src/models/FGAerodynamics.cpp \
	JSB-FlightSim/src/models/FGAircraft.cpp \
	JSB-FlightSim/src/models/FGAtmosphere.cpp \
	JSB-FlightSim/src/models/FGAuxiliary.cpp \
	JSB-FlightSim/src/models/FGBuoyantForces.cpp \
	JSB-FlightSim/src/models/FGExternalForce.cpp \
	JSB-FlightSim/src/models/FGExternalReactions.cpp \
	JSB-FlightSim/src/models/FGFCS.cpp \
	JSB-FlightSim/src/models/FGGasCell.cpp \
	JSB-FlightSim/src/models/FGGroundReactions.cpp \
	JSB-FlightSim/src/models/FGInertial.cpp \
	JSB-FlightSim/src/models/FGInput.cpp \
	JSB-FlightSim/src/models/FGLGear.cpp \
	JSB-FlightSim/src/models/FGMassBalance.cpp \
	JSB-FlightSim/src/models/FGModel.cpp \
	JSB-FlightSim/src/models/FGOutput.cpp \
	JSB-FlightSim/src/models/FGPropagate.cpp \
	JSB-FlightSim/src/models/FGPropulsion.cpp \
	JSB-FlightSim/src/models/FGSurface.cpp \
	JSB-FlightSim/src/models/atmosphere/FGMSIS.cpp \
	JSB-FlightSim/src/models/atmosphere/FGMSISData.cpp \
	JSB-FlightSim/src/models/atmosphere/FGMars.cpp \
	JSB-FlightSim/src/models/atmosphere/FGStandardAtmosphere.cpp \
	JSB-FlightSim/src/models/atmosphere/FGWinds.cpp \
	JSB-FlightSim/src/models/flight_control/FGAccelerometer.cpp \
	JSB-FlightSim/src/models/flight_control/FGActuator.cpp \
	JSB-FlightSim/src/models/flight_control/FGAngles.cpp \
	JSB-FlightSim/src/models/flight_control/FGDeadBand.cpp \
	JSB-FlightSim/src/models/flight_control/FGDistributor.cpp \
	JSB-FlightSim/src/models/flight_control/FGFCSComponent.cpp \
	JSB-FlightSim/src/models/flight_control/FGFCSFunction.cpp \
	JSB-FlightSim/src/models/flight_control/FGFilter.cpp \
	JSB-FlightSim/src/models/flight_control/FGGain.cpp \
	JSB-FlightSim/src/models/flight_control/FGGyro.cpp \
	JSB-FlightSim/src/models/flight_control/FGKinemat.cpp \
	JSB-FlightSim/src/models/flight_control/FGLinearActuator.cpp \
	JSB-FlightSim/src/models/flight_control/FGMagnetometer.cpp \
	JSB-FlightSim/src/models/flight_control/FGPID.cpp \
	JSB-FlightSim/src/models/flight_control/FGSensor.cpp \
	JSB-FlightSim/src/models/flight_control/FGSummer.cpp \
	JSB-FlightSim/src/models/flight_control/FGSwitch.cpp \
	JSB-FlightSim/src/models/flight_control/FGWaypoint.cpp \
	JSB-FlightSim/src/models/propulsion/FGBrushLessDCMotor.cpp \
	JSB-FlightSim/src/models/propulsion/FGElectric.cpp \
	JSB-FlightSim/src/models/propulsion/FGEngine.cpp \
	JSB-FlightSim/src/models/propulsion/FGForce.cpp \
	JSB-FlightSim/src/models/propulsion/FGNozzle.cpp \
	JSB-FlightSim/src/models/propulsion/FGPiston.cpp \
	JSB-FlightSim/src/models/propulsion/FGPropeller.cpp \
	JSB-FlightSim/src/models/propulsion/FGRocket.cpp \
	JSB-FlightSim/src/models/propulsion/FGRotor.cpp \
	JSB-FlightSim/src/models/propulsion/FGTank.cpp \
	JSB-FlightSim/src/models/propulsion/FGThruster.cpp \
	JSB-FlightSim/src/models/propulsion/FGTransmission.cpp \
	JSB-FlightSim/src/models/propulsion/FGTurbine.cpp \
	JSB-FlightSim/src/models/propulsion/FGTurboProp.cpp \
	JSB-FlightSim/src/simgear/xml/easyxml.cxx \
	JSB-FlightSim/src/simgear/xml/xmlparse.cpp \
	JSB-FlightSim/src/simgear/xml/xmlrole.cpp \
	JSB-FlightSim/src/simgear/xml/xmltok.cpp \
	JSB-FlightSim/src/simgear/io/iostreams/sgstream.cxx \
	JSB-FlightSim/src/simgear/magvar/coremag.cxx \
	JSB-FlightSim/src/simgear/misc/sg_path.cxx \
	JSB-FlightSim/src/simgear/misc/strutils.cxx \
	JSB-FlightSim/src/simgear/props/props.cxx)
SPEC_CFLAGS += -DSPEC_AUTO_BYTEORDER=0x12345678 -Isrc/JSB-FlightSim/src -Isrc/JSB-FlightSim/src/simgear/xml -DXML_POOR_ENTROPY -DJSBSIM_STATIC_LINK -DSPEC_AUTO_SUPPRESS_THREADING
SPEC_CXXFLAGS += 
SPEC_FFLAGS += 
SPEC_LDFLAGS += -lm
LD_CXX = 1
include ../Makefile.apps
include ../Makefile.run
.PHONY: clean_preprocess_objs
clean_preprocess_objs:

refrate-cmp:
	$(call SPECDIFF, --abstol 0.0001, $(RUN_DIR)/B747_script1.xml.out, data/refrate/output/B747_script1.xml.out)
	$(call SPECDIFF, --abstol 0.0070, $(RUN_DIR)/ah1s_flight_test.xml.out, data/refrate/output/ah1s_flight_test.xml.out)
	$(call SPECDIFF, --abstol 0.0800, $(RUN_DIR)/ball_orbit.xml.out, data/refrate/output/ball_orbit.xml.out)
	$(call SPECDIFF, --abstol 0.0001, $(RUN_DIR)/ball_orbit_g_torque.xml.out, data/refrate/output/ball_orbit_g_torque.xml.out)
	$(call SPECDIFF, --abstol 0.0001 --reltol 0.0170, $(RUN_DIR)/ball_orbit_g_torque2.xml.out, data/refrate/output/ball_orbit_g_torque2.xml.out)
	$(call SPECDIFF, --abstol 0.5800, $(RUN_DIR)/c3104.xml.out, data/refrate/output/c3104.xml.out)
	$(call SPECDIFF, --abstol 0.0001 --reltol 0.0010, $(RUN_DIR)/weather-balloon2.xml.out, data/refrate/output/weather-balloon2.xml.out)
	$(call SPECDIFF, --abstol 0.0005, $(RUN_DIR)/x153.xml.out, data/refrate/output/x153.xml.out)
train-cmp:
	$(call SPECDIFF, --abstol 0.0001, $(RUN_DIR)/Short_S23_2.xml.out, data/train/output/Short_S23_2.xml.out)
	$(call SPECDIFF, --abstol 0.0140, $(RUN_DIR)/c3105.xml.out, data/train/output/c3105.xml.out)
	$(call SPECDIFF, --abstol 0.9600, $(RUN_DIR)/f16_test.xml.out, data/train/output/f16_test.xml.out)
	$(call SPECDIFF, --abstol 0.0001 --reltol 0.0010, $(RUN_DIR)/weather-balloon.xml.out, data/train/output/weather-balloon.xml.out)
test-cmp:
	$(call SPECDIFF, --abstol 0.0100, $(RUN_DIR)/J2461.xml.out, data/test/output/J2461.xml.out)
	$(call SPECDIFF, --abstol 0.0900, $(RUN_DIR)/c1722.xml.out, data/test/output/c1722.xml.out)
