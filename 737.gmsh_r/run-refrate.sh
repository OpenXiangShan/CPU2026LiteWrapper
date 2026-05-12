$APP -option gmsh.opts -nt 0 choi.geo > choi.geo.out 2> choi.geo.err
$APP -option gmsh.opts -nt 0 mediterranean.geo > mediterranean.geo.out 2> mediterranean.geo.err
$APP -option gmsh.opts -nt 0 projection.geo > projection.geo.out 2> projection.geo.err
$APP -option gmsh.opts -nt 0 gasdis.geo > gasdis.geo.out 2> gasdis.geo.err
$APP -option gmsh.opts -nt 0 Torus.geo > Torus.geo.out 2> Torus.geo.err
$APP -option gmsh.opts -nt 0 spec.geo -clscale 0.175 -algo del2d -algo hxt > spec.geo.out 2> spec.geo.err
$APP -option gmsh.opts -nt 0 p19.geo > p19.geo.out 2> p19.geo.err
