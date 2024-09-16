def F(x, y, z, w):
    l1 = x or not(y)
    l2 = not(z) == w
    l3 = y and z
    return (l1 and l2) == l3

for x in 1,0:
    for y in 1, 0:
        for z in 1, 0:
            for w in 1, 0:
                if F(x, y, z, w) == 0:
                    print(x, y, z, w)

#
#                                       w
#   x y z w |                           z
#               1 1 1 1             1 _ 1 1
#   1 1 1 1     0 1 1 1             0 0 _ 0
#   1 1 0 1     1 1 0 1             0 _ _ 1
#   1 0 1 0
#   1 0 0 1     0 0 0 1
#   0 1 1 1     0 0 1 0
#   0 1 1 0
#   0 0 1 0     0 1 1 0
#   0 0 0 1     1 0 0 1
#               1 0 1 0
#               0 0 1 0 -30
#               0 0 0 1 -30
#               1 1 0 1 -31
#               0 1 1 1 -31
#
#
#
#
#
#
