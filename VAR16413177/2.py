for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not ((x or y) <= (y == z)):
                print(x, y, z)
# x y z
# 0 1 0
# 1 0 1
# 1 1 0
#
#z x y
#0 0 _
#0 _ _
#
#
#