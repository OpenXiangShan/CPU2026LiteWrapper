$APP --memdb --size 2000 --testset main --verify > sqlite_r.main.out 2> sqlite_r.main.err
$APP --memdb --size 2000 --testset cte --verify > sqlite_r.cte.out 2> sqlite_r.cte.err
$APP --memdb --size 1000 --testset fp --verify > sqlite_r.fp.out 2> sqlite_r.fp.err
