#! /bin/bash

for file_number in {1..10}; do

	touch "test$file_number.txt"

	echo "Файл test$file_number.txt создан!" 

done


file_number=11

while [ $file_number -gt 1 ]; do


   ((file_number--))

    rm "test$file_number.txt"

 echo "Файл test$file_number.txt успешно удален!"

done


