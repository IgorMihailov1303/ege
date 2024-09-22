def F(p,r):
    if p == r:
        return 1
    elif p >= r:
        return 0
    return F(p+1,r) + F(p+2,r) + F(p+5,r)
print(F(21,30))
