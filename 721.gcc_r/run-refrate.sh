$APP gcc-pp.c -O2 -fpic -o gcc-pp.c.opts-O2_-fpic.s > gcc-pp.c.opts-O2_-fpic.s.out 2> gcc-pp.c.opts-O2_-fpic.s.err
$APP gcc-smaller.c -O3 -fipa-pta -o gcc-smaller.c.opts-O3_-fipa-pta.s > gcc-smaller.c.opts-O3_-fipa-pta.s.out 2> gcc-smaller.c.opts-O3_-fipa-pta.s.err
$APP ref32.c -O3 -finline-limit=12000 -fno-tree-vrp -o ref32.c.opts-O3_-finline-limit_12000_-fno-tree-vrp.s > ref32.c.opts-O3_-finline-limit_12000_-fno-tree-vrp.s.out 2> ref32.c.opts-O3_-finline-limit_12000_-fno-tree-vrp.s.err
