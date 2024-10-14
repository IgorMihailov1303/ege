from itertools import *

s = sorted('012435678')
r = list(product(s, repeat=5))
x = set()
d = ''
for i in r:
    i = sorted(i,reverse=-1)
    if i[0] > i[1] > i[2] > i[3] > i[4]:
        d = ''.join(i)
        x.add(d)
print(x)
print(len(x))

