def middle_result(d, base_payday, const):
    assert type(d) == dict
    array = []
    for i in d.values():
        array.append(i)
    middle = float((sum(array) / len(array)))
    if middle >= 3.5 and middle < 4.5:
        return float(base_payday) * int(const)
    elif middle >= 4.5 and array <= 5:
        return float(base_payday) * int(const) * 1.5
    elif middle < 3.5:
        return "Стипендия не выплачивается"

dictionary = {'a': 4, 'b': 3, 'c': 5}
print(middle_result(dictionary, 2310, 1))