a = [int(i) for i in input().split()]
b = []
x = int(input())
if x not in a:
    print("Отсутствует")
else:
    for i in range(len(a)):
        if x == a[i]:
            b.append(i)
    print(*b)