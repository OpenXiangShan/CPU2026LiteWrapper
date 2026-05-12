$APP transformsplus.bc -S -O3 -mcpu=pwr9 --sha512 -o transformsplus.bc.opts-S_-O3_-mcpu_pwr9.ll > transformsplus.bc.opts-S_-O3_-mcpu_pwr9.out 2> transformsplus.bc.opts-S_-O3_-mcpu_pwr9.err
$APP codegen.bc -S -O3 -mcpu=pwr9 --sha512 -o codegen.bc.opts-S_-O3_-mcpu_pwr9.ll > codegen.bc.opts-S_-O3_-mcpu_pwr9.out 2> codegen.bc.opts-S_-O3_-mcpu_pwr9.err
