from itertools import *

def Usl1(x, y, z, w):
    l1 = x or not(y)
    l2 = w==z
    return l1 <= l2
def Usl2(x, y, z, w):
    l1 = x or not(y)
    l2 = w <= z
    return l1 == l2

for a1, a2, a3, a4, a5, a6 in product([1,0], repeat=6):
    tab = [(0, a1, 0, 0), (a2, 1, 1, a3), (a4, 0, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if ([Usl1(**dict(zip(p,r))) for r in tab] == [0,0,a5]) and ([Usl2(**dict(zip(p,r))) for r in tab] == [0,a6,0]):
                print(p)