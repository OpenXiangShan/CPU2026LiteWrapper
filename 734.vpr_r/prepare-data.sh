#!/bin/bash
# Decompress .xz files for vpr
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    if [ -d "${INPUT_DIR}" ]; then
        for xzfile in ${INPUT_DIR}/*.xz; do
            [ -f "$xzfile" ] || continue
            echo "Decompressing $xzfile..."
            xz -dk "$xzfile" 2>/dev/null || true
        done
    fi
done
