print("=== Анализ последовательности ДНК ===")

dna_str = input ("Введите последовательность ДНК:")
dna = str(dna_str)
dna_up = dna.upper()

print (f"Последовательность в верхнем регистре:\t {dna_up}")

print ("Подсчет нуклеотидов:")

count_A = dna_up.count("A")
count_T = dna_up.count("T")
count_G = dna_up.count("G")
count_C = dna_up.count("C")

dna_sum = count_A + count_T + count_G + count_C

print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")


print (f"Общая длина: {dna_sum} нуклеотидов") 