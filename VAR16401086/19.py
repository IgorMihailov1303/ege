def f(c, p):
    if c > 64 and p == 3:
        return True
    if c <= 64 and p == 3:
        return False
    if c > 64:
        return False
    else:
        return f(c + 1, p + 1) or f(c + 2, p + 1) or f(c * 3, p + 1)

for S in range(1, 64 + 1):
    if f(S, 1):
        print(S)