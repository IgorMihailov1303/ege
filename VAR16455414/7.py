r = []
for a in range(1000, 10000):
    a = str(a)
    c = []
    c.append(str(int(a[0]) + int(a[1])))
    c.append(str(int(a[1]) + int(a[2])))
    c.append(str(int(a[2]) + int(a[3])))
    d = c.sort(reverse=True)
    if (c[1] + c[0]) == '1315':
        r.append(a)
print(max(r))