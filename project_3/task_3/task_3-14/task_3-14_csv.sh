#!/bin/bash

echo "Названия товаров:"

awk -F "," 'NR > 1 {print $2}' data.csv 

echo "Все товары, дороже 20:"

awk -F ", *" '$3 > 20 {print $2, $3}' data.csv

awk -F ", *" '{sum += $3} END {print "Общая стоимость: " sum}' data.csv
 
