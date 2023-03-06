a = [str(i) for i in input().lower().split()]
b = []
word_count = {}
for i in a:
    if  i not in word_count:
        word_count[i] = a.count(i)
print(word_count)
for k in word_count.keys():
    b.append(word_count[k])
print(*b)