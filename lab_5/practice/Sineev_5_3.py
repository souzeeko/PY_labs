a = [int(i) for i in input().split()]
maxa = a.index(max(a))
mina = a.index(min(a))
a[maxa], a[mina] = a[mina], a[maxa]
print(*a)