#!/bin/bash

for NUMBER in {1..20}; do
    
    
    if [ $NUMBER -eq 15 ]; then
        echo "Встретили число 15! Останавливаемся."
        break
    fi
    
      if [ $((NUMBER % 2)) -eq 0 ]; then
        continue
    fi
    
    echo "$NUMBER"
    
done
