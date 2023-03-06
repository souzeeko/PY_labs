a = [int(i) for i in input().split()]
print(*sorted(a[::2], reverse = True))