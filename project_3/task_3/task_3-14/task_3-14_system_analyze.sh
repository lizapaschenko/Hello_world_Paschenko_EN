#!/bin/bash

echo "=== Анализ дискового пространства ==="
echo ""

df -h | awk '
NR > 1 {
    filesystem = $1
    percent = $5
    gsub(/%/, "", percent)
    
    print filesystem, $5
    
    if (percent > 90) {
        print "  ВНИМАНИЕ! " filesystem " заполнен на " $5
    }
}'
