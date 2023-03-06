g_str = input().lower()
xtimes = ''
count = 1
character = g_str[0]
for i in range(1, len(g_str)):
    if g_str[i] == character:
        count += 1
    else:
        xtimes += character + str(count)
        character = g_str[i]
        count = 1
xtimes += character + str(count)
print(xtimes)