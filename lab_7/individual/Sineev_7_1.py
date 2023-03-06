def modify_list(lst):
    for i in reversed(range(len(lst))):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
        else:
            del lst[i]

# l = [int(i) for i in input().split()]
# modify_list(l)
# print(l)