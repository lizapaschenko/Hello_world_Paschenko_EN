A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
D = float(input("Введите D: "))

min_val = A

if not (A < B):
    min_val = B

if not (min_val < C):
    min_val = D

print("min =", min_val)