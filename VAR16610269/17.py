a = 49**10 + 7**30 - 49
s = ''
while a != 0:
    s += str(a % 7)
    a //= 7
s = s[::-1]
print(s.count("6"))