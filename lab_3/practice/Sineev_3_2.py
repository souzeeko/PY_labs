n = int(input())
a = []
for i in range(1, n + 1):
    j = 0
    while j < i:
        a.append(i)
        j += 1
    if len(a) > n: 
        break
a = a[0 : n]
print(*a)