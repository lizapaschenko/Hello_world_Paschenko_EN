# Создание логов прибора

fio = input ("Введите имя оператора:")
pressure = input ("Введите текущее значение давление (Па):")
with open("sensor_log.txt", "w", encoding="utf-8") as table:
     table.write(f"(Имя оператора:\t {fio}")
     table.write(f"(Давление:\t {pressure}")
     print ("Данные успешно сохранены в sensor_log.txt") 