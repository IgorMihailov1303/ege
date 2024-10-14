from itertools import *

x = []
s = 'МАТВЕЙ'
r = list(permutations(s, 6))
for i in r:
    if i[0] != 'Й' and (i[0]+i[1]!='АЕ') and (i[1]+i[2]!='АЕ') and (i[2]+i[3]!='АЕ') and (i[3]+i[4]!='АЕ') and (i[4]+i[5]!='АЕ'):
        x.append(i)
print(len(x))