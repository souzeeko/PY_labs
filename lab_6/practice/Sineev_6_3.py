a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = set()
for i in a:
    for j in b:
        if i == j:
            c.add(i)
print(len(c))