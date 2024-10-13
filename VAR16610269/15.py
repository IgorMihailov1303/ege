from itertools import product
r = []
n = 0
for i in product('12', repeat=13):
    i = str(''.join(i))
    if i.count('1') == 10 and i.count('2') == 3:
        if not(i in r):
            r.append(i)
for a in r:
    c = 0
    while '11' in a:
        if '112' in a:
            a = a.replace('112','6',1)
        else:
            a = a.replace('11','3',1)
    for k in a:
        c = c + int(k)
    if c > n:
        n = c

print(n)
