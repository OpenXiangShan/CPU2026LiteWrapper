#!/bin/bash
# Decompress OBJ-values.dat.xz for each size
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    if [ -f "${INPUT_DIR}/OBJ-values.dat.xz" ]; then
        echo "Decompressing ${INPUT_DIR}/OBJ-values.dat.xz..."
        xz -dk "${INPUT_DIR}/OBJ-values.dat.xz" 2>/dev/null || true
    fi
done
