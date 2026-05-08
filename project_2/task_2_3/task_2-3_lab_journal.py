# task_2-3_lab_journal.py

# Сбор данных
print("Электронный лабораторный журнал")
fio = input("ФИО исследователя: ")
date = input("Дата: ")
experiment_name = input("Эксперимент: ")
conclusion = input("Вывод: ")

# Задаем фиксированную ширину рамки
WIDTH = 60
CONTENT_WIDTH = WIDTH - 6  # Ширина для текста внутри рамки (с учетом '| ' и ' |')

def separator():
    """Создает разделительную линию"""
    return "+" + "-" * (WIDTH-2) + "+"

def line_with_border(text):
    """Создает строку с рамкой для текста"""
    return f"| {text:<{CONTENT_WIDTH}} |"

def split_text(text, max_width):
    """Разбивает текст на строки заданной ширины с учетом целостности слов"""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        # Проверяем, поместится ли слово в текущую строку
        if len(current_line) + len(word) + 1 <= max_width:
            if current_line:
                current_line += " " + word
            else:
                current_line = word
        else:
            # Сохраняем текущую строку и начинаем новую
            if current_line:
                lines.append(current_line)
            current_line = word
    
    # Добавляем последнюю строку
    if current_line:
        lines.append(current_line)
    
    return lines

# Открываем файл для записи
with open("journal.txt", "w", encoding="utf-8") as journal:
    # Верхняя граница
    top = separator()
    print(top)              # Вывод на экран
    journal.write(top + "\n")  # Запись в файл
    
    # Заголовок
    title = f"| {'ЭЛЕКТРОННЫЙ ЛАБОРАТОРНЫЙ ЖУРНАЛ':^{CONTENT_WIDTH}} |"
    print(title)             # Вывод на экран
    journal.write(title + "\n")  # Запись в файл
    
    # Разделитель
    sep = separator()
    print(sep)              # Вывод на экран
    journal.write(sep + "\n")  # Запись в файл
    
    # Данные исследователя
    fio_line = line_with_border(f"ФИО исследователя: {fio}")
    date_line = line_with_border(f"Дата: {date}")
    exp_line = line_with_border(f"Эксперимент: {experiment_name}")
    
    print(fio_line)          # Вывод на экран
    print(date_line)         # Вывод на экран
    print(exp_line)          # Вывод на экран
    journal.write(fio_line + "\n")   # Запись в файл
    journal.write(date_line + "\n")  # Запись в файл
    journal.write(exp_line + "\n")   # Запись в файл
    
    # Разделитель перед выводом
    print(sep)               # Вывод на экран
    journal.write(sep + "\n")   # Запись в файл
    
    # Заголовок вывода
    conclusion_header = line_with_border("ВЫВОД:")
    print(conclusion_header)  # Вывод на экран
    journal.write(conclusion_header + "\n")  # Запись в файл
    
    # Разбиваем длинный вывод на строки
    conclusion_lines = split_text(conclusion, CONTENT_WIDTH)
    
    # Выводим каждую строку вывода
    for line in conclusion_lines:
        bordered_line = line_with_border(line)
        print(bordered_line)   # Вывод на экран
        journal.write(bordered_line + "\n")  # Запись в файл
    
    # Нижняя граница
    bottom = separator()
    print(bottom)            # Вывод на экран
    journal.write(bottom + "\n")  # Запись в файл





