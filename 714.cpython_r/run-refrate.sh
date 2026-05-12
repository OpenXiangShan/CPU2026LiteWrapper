$APP -I -B coreml_pb.py -i 2 -a -m Resnet50Headless.mlmodel -d 10 > cpython_r_0.out 2> cpython_r_0.err
$APP -I -B coreml_pb.py -i 5 -a -c -m MobileNetV2.mlmodel -d 20 > cpython_r_1.out 2> cpython_r_1.err
$APP -I -B dna_bench.py 600000 > cpython_r_2.out 2> cpython_r_2.err
