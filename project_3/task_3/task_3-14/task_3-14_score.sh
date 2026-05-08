#!/bin/bash

echo "=== Студенты с оценкой выше 80 ==="
awk '$2 > 80 {print $1, $2}' students.txt

echo ""
echo "=== Студенты с оценкой ниже 70 ==="
awk '$2 < 70 {print $1, $2}' students.txt

echo ""
echo "=== Только первая строка ==="
awk 'NR == 1 {print $0}' students.txt
