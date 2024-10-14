from itertools import *

s = sorted('АБЗИ')
cnt = 0
for i in list(product(s, repeat=4)):
    print(i)
    cnt += 1
    if i == ('И','З','Б','А'):
        print(cnt)
        break