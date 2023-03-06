a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = input("Введите название операции (+, -, /, *, div, mod, pow): ")
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Деление на 0!")
elif c == "*":
    print(a * b)
elif c == "div":
    print(a // b)
elif c == "mod":
    print(a % b)
elif c == "pow":
    print(a**b)