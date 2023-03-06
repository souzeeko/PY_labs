a = [int(s) for s in input().split()]
b = []
s = 0
for elem in a:
    s += elem
avg = s / len(a)
for elem in a:
    if elem >= avg:
        b.append(elem)
print('Среднее арифметическое равно', int(avg))
print('Всего значений больше среднего арифметического:', len(b))
print('Список значений:', *b)