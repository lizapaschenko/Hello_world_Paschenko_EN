#!/bin/bash

read -p "Введите ваш вес (в кг): " WEIGHT
read -p "Введите ваш рост (в см, например 175): " HEIGHT

BMI=$(( ($WEIGHT * 10000) / ($HEIGHT * $HEIGHT) ))

echo "Ваш индекс массы тела (ИМТ): $BMI"
