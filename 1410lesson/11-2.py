from itertools import *

s = 'РОСОМАХА'
s1 = 'РСМХ'
s2 = 'ООАА'

r = list(product(s1,s2,s1,s2,s1,s2,s1,s2))+list(product(s2,s1,s2,s1,s2,s1,s2,s1))
x = []

for i in r:
    if i.count('Р')==1 and i.count('С')==1 and i.count('М')==1 and i.count('Х')==1 and i.count('О')==2 and i.count('А')==2:
        x.append(i)
print(len(x))