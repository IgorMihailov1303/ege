from itertools import *
def Usl(x, y, z, w):
    l1 = x and not(y)
    l2 = not(z) or not(w)
    l3 = w <= x
    return int((l1 <= l2) and (l3 or y))


for a1, a2, a3, a4, a5, a6 in product([1,0], repeat=6):
    tab = [(1, a1, 1, 1), (0, a2, a3, 0), (1, a4, a5, a6)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [Usl(**dict(zip(p,r))) for r in tab] == [0,0,0]:
                print(p)
