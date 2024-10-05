a = open('11.txt')
b = 0
for i in a:
    c = [int(j) for j in i.split()]
    l = []
    for x in c:
        if c.count(x) == 2:
            l.append(x)
        if c.count(x) > 2:
            break
    if len(l) == 4 and len(set(l)) == 2:
        if sum(l)/4 < (sum(c) - sum(l))/3:
            b += 1
print(b)