from itertools import *

s = sorted("ВЕРОНИКА")
r = list(product(s, repeat=3))


rs = ["0А"]
for i in range(0, len(r)-1):
    if r[i].count('В') == 1:
        rs.append(r[i])

cnt = 0
for i in range(0,len(rs)-1):
    if 'А' not in rs[i]:
        print(cnt, rs[i])
        break
    else:
        cnt += 1

print(rs)
