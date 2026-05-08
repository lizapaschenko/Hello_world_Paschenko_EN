#!/bin/bash

echo "Сумма оценок:"

awk '{sum += $2} END {print sum}' students.txt

echo "Средняя оценка:"

awk '{sum += $2; n++} END {print sum/n}' students.txt

echo "Максимальная оценка:"

awk 'NR==1 {max=$2} $2>max {max=$2} END {print max}' students.txt 
