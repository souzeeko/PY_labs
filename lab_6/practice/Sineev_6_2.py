d = {str(i): str(i + 1) for i in range(1, 11)}
inverted_d = {value: key for key, value in d.items()}
v = input("value: ")
print(inverted_d.get(v, "value is not in dictionary"))