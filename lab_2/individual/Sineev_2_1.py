A = int(input("А: "))
B = int(input("B: "))
H = int(input("H: "))
if H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
else:
    print("Это нормально")