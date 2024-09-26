letters7 = '0123456'
letters9 = '012345678'
a1l = []
a2l = []
for y in letters7:
    for x in letters7:
        a1 = int(x + y + '320', 7)
        a1l.append(a1)

for y in letters9:
    for x in letters9:
        a2 = int('1' + x + '3' + y +'3', 9)
        a2l.append(a2)

minsum = []
for i in range(len(a1l)):
    for j in range(len(a2l)):
        if (a1l[i] + a2l[j]) % 181 == 0:
            minsum.append((a1l[i] + a2l[j]))
print(minsum)
print(min(minsum) // 181)
