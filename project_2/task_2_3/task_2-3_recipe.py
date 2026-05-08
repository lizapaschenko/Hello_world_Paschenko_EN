#Создание рецептурного справочника

nutrient_medium = input ("Введите название питательной среды:")
consentration = input ("Введите концентрацию агара (%):")
temperature = input ("Введите температуру стерилизации (°C):")
with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"(Название питательной среды:\t{nutrient_medium}\n")
    recipe.write(f"Концентрация агара (%):\t{consentration}\n")
    recipe.write(f"Температура стерилизации (°C):\t{temperature}")

print("Файл 'recipe.txt' успешно сформирован!")

