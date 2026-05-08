weight_int = input ("Введите ваш вес (кг):")
height_int = input ("Введите ваш рост (см):")
weight = int (weight_int)
height = int (height_int)
bmi = weight / (height ** 2)
print ("--- Отчет о состоянии здоровья ---")
print (f"Рост:\t{height:.1f} см \nВес:\t{weight:.1f} кг\nИндекс массы тела: {bmi:.2f}") # .2f округлит до 2 знаков

