volume = float(input("Введите нужный объем физиологического раствора (в мл): "))
salt_mass = volume * 0.009
print(f"\nДля приготовления {volume} мл физиологического раствора:")
print(f"Потребуется: {salt_mass:.2f} г соли и {volume:.2f} мл воды")
with open("recipe.txt", "w", encoding="utf-8") as file:
 file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
 file.write("-" * 23 + "\n")
 file.write(f"Общий объем: {volume:.2f} мл\n")
 file.write(f"Масса соли: {salt_mass:.2f} г\n")
 file.write(f"Объем воды: {volume:.2f} мл\n")
print("\nРецепт успешно сохранен в файл recipe.txt")