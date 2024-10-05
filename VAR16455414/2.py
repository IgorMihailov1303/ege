print("x y z w")

for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((y <= z) and not((y or w) <= (z and w)))
                if F == 1:
                    print(x, y, z, w)

#
#x y z w
#0 1 1 0
#1 0 0 1
#1 1 1 0

#
#1 1 0 1
#0 1 1 0
#1 1 0 _