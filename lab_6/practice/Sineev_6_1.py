import random
d = {str(i): random.randint(-10, 10) for i in range(1, 11)}
k = input("key: ")
print(d.get(k, "key is not in dictionary"))