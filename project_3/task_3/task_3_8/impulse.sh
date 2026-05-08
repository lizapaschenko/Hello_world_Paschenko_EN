#!/bin/bash

read -p "Введите имя гена: " GEN_NAME
read -p "Введите уровень экспрессии (целое число): " EXPRESSION_LEVEL

if [ -z "$GEN_NAME" ] || [ -z "$EXPRESSION_LEVEL" ]; then
    echo "Недостаточно данных"
else
    echo "Экспрессия гена $GEN_NAME составляет $EXPRESSION_LEVEL единиц"
fi
