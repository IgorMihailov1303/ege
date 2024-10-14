from itertools import *

s = sorted('МАНГУСТ')

cnt = 0
lcnt = 0
x = []
for i in list(product(s, repeat=6)):
    cnt += 1
    if i[0]!='У' and i.count('М')==2 and i.count('Г')<=1:
        x.append(i)
        lcnt = cnt
print(x[-1], lcnt)
