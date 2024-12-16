def usl(x, A):
    l1 = x&28 != 0
    l2 = x&45 != 0
    l12 = l1 or l2
    l3 = x&17 == 0
    l4 = x%A != 0
    l34 = l3 <= l4
    return int(l12 <= l34)

c = 0
while c != 1:
    for A in range(1, 1000):
        for x in range(1, 1000):
            c += usl(x, A)
print(A)