N = int(input("Введите N: "))

if N <= 0:
    print("Ошибка. N должно быть больше 0")
else:
    # Ввод первого числа
    max_val = float(input("Введите число: "))
    i = 2
    while i <= N:
        x = float(input("Введите число: "))
        if x > max_val:          # Если текущее число больше максимума, обновляем максимум
            max_val = x
        i = i + 1
    print(max_val)