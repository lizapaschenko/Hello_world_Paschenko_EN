pills_total_int = input ("Введите общее количество произведенных капсул: ")
pills_total = int (pills_total_int)
pills_in_1_pack_int = input ("Введите количество капсул в одной упаковке: ")
pills_in_1_pack = int (pills_in_1_pack_int)
packs_total = pills_total // pills_in_1_pack
extra_pills = pills_total % pills_in_1_pack
print(f"--- Отчет фасовачного цеха ---\nПолных упаковок:\t{packs_total}\nОстаток капсул:\t{extra_pills}")