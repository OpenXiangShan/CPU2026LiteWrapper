#!/bin/bash
# Decompress .xz files for gem5
for size in test train refrate; do
    INPUT_DIR="data/${size}/input"
    GEN_FILE="${INPUT_DIR}/control.gen"
    if [ -f "${GEN_FILE}" ]; then
        while IFS= read -r line; do
            [ -z "$line" ] && continue
            [[ "$line" = \#* ]] && continue
            xzfile="${INPUT_DIR}/${line}.xz"
            if [ -f "$xzfile" ]; then
                echo "Decompressing $xzfile..."
                xz -dk "$xzfile" 2>/dev/null || true
            fi
        done < "${GEN_FILE}"
    fi
done
