$APP mobile-scenario --simTimeMinutes=3 --RngSeed=1 --RngRun=1 > mobile-scenario_0.out 2> mobile-scenario_0.err
$APP tcp-pacing --simulationEndTime=500 --useEcn=false --RngSeed=1 --RngRun=1 > tcp-pacing_1.out 2> tcp-pacing_1.err
$APP lena-radio-link-failure --numberOfEnbs=2 --interSiteDistance=800 --simTime=200 --RngSeed=1 --RngRun=1 > lena-radio-link-failure_2.out 2> lena-radio-link-failure_2.err
$APP dctcp-example --enableSwitchEcn=true --flowStartupWindow=0.4 --convergenceTime=0.4 --measurementWindow=0.4 --RngSeed=1 --RngRun=1 > dctcp-example_3.out 2> dctcp-example_3.err
$APP wifi-mixed-network --isUdp=0 --payloadSize=3072 --simulationTime=25 --RngSeed=1 --RngRun=1 > wifi-mixed-network_4.out 2> wifi-mixed-network_4.err
$APP wifi-eht-network --simulationTime=0.2 --frequency=5 --useRts=1 --minExpectedThroughput=6 --maxExpectedThroughput=547 --RngSeed=1 --RngRun=1 > wifi-eht-network_5.out 2> wifi-eht-network_5.err
