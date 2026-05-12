$APP -I -B coreml_pb.py -i 10 -a -c -m PoseNetMobileNet100S16FP16.mlmodel > cpython_r_0.out 2> cpython_r_0.err
$APP -I -B dna_bench.py 200000 > cpython_r_1.out 2> cpython_r_1.err
