$APP -option gmsh.opts -nt 0 sphere-discrete.geo > sphere-discrete.geo.out 2> sphere-discrete.geo.err
$APP -option gmsh.opts -nt 0 spec.geo -smooth 2 -clscale .27 > spec.geo.out 2> spec.geo.err
