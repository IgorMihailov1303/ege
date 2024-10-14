from itertools import *

x = []
s = 'ГЕРАСИМ'
s1 = 'ГРСМ'
s2 = 'ЕАИ'

r = list(product(s1, s2, s1, s2, s1, s2, s1))
for i in r:
    print(i, set(i))
    if len(i) == len(set(i)):
        x.append(i)
print(len(x))
