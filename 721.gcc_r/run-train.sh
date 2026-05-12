$APP 200.c -O2 -o 200.c.opts-O2.s > 200.c.opts-O2.s.out 2> 200.c.opts-O2.s.err
$APP scilab.c -O3 -o scilab.c.opts-O3.s > scilab.c.opts-O3.s.out 2> scilab.c.opts-O3.s.err
$APP train01.c -O3 -finline-limit=50000 -o train01.c.opts-O3_-finline-limit_50000.s > train01.c.opts-O3_-finline-limit_50000.s.out 2> train01.c.opts-O3_-finline-limit_50000.s.err
