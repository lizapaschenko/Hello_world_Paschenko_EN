#!/bin/bash


printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"
echo "-------------------------------------------------------"


for file in *.fasta; do
    
    
    if [ ! -s "$file" ]; then
        continue
    fi
    
    
    SEQUENCE=$(grep -v "^>" "$file" | tr -d '\n')
    
   
    A_COUNT=$(echo "$SEQUENCE" | grep -o "A" | wc -l)
    T_COUNT=$(echo "$SEQUENCE" | grep -o "T" | wc -l)
    G_COUNT=$(echo "$SEQUENCE" | grep -o "G" | wc -l)
    C_COUNT=$(echo "$SEQUENCE" | grep -o "C" | wc -l)
    
    
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A_COUNT" "$T_COUNT" "$G_COUNT" "$C_COUNT"
    
done
