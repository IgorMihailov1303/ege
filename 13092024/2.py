def F(x, y, z, w):
    l1 = x and not(y)
    l2 = x == z
    l3 = not(w)
    return int(l1 or l2 or l3)

print('x y z w | F(x, y, z, w)')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if F(x, y, z, w) == 0:
                    print(x, y, z, w, '|', F(x, y, z, w))

#W в первом столбце (единственный с тремя единицами), X в последнем столбце(единственный с двумя нулями), Z во втором столбце(инверсия X), Y в третьем столбце(исклюением)
