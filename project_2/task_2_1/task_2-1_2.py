researcher_name = "Роднова Т.В."
date = "10.02.2026"
experiment_name = "Клонирование"
conclusion = "Создали клона человека"
with open('journal.txt', 'w', encoding='utf-8') as file:
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"|{'Электронный лабораторный журнал'.center(50)}|\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| Дата              : {date}\n")
    file.write(f"| Эксперимент       : {experiment_name}\n")
    file.write("+" + "-" * 50 + "+\n")
    file.write(f"| Вывод: {conclusion}\n")
    file.write("+" + "-" * 50 + "+\n")
    