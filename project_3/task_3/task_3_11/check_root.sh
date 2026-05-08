#!/bin/bash

check_root() {
    if [ $EUID -eq 0 ]; then
        return 0
    else
        echo "Ошибка: Скрипт должен быть запущен от имени суперпользователя!"
        
        return 1
    fi
}

check_root


if [ $? -ne 0 ]; then
     exit 1
fi


echo "Скрипт запущен от имени суперпользователя. Успех!"

