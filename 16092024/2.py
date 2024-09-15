def F(x, y, z, w):
    l1 = y or z
    l2 = z and w
    l3 = x and z
    l4 = w or y
    l34 = (l3 <= l4)
    l12 = (l1 <= l2)
    return int(l12 != l34)

print('x y z w | F(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w) == 1:
                    print(x, y, z, w, '|', F(x, y, z, w))
#             y
#x y z w    w x x z         WYXZ
#1 1 0 1    0 1 1 1
#1 1 1 0    0 0 0 1
#           1 1 0 0
#0 1 0 0
#0 0 1 0

#1 1 0 0
#0 1 1 0
#0 1 0 1
