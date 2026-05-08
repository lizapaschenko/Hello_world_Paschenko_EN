#!/bin/bash



echo "=== Имена студентов ==="
awk '{print $1}' students.txt

echo ""
echo "=== Оценки студентов ==="
awk '{print $2}' students.txt

echo ""
echo "=== Номер строки и имя ==="
awk '{print NR, $1}' students.txt
