g_str = input().upper()
GC = g_str.count('G') + g_str.count('C')
print('GC concentration is ' + str(float(GC / len(g_str) * 100)) + '%')