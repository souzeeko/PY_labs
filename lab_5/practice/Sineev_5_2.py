a = [int(i) for i in input().split()]
b = []
for i in range(len(a) - 1):
    if a[i + 1] > a[i]:
        b.append(a[i + 1])
print(*b)