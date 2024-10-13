def f(c, p):
    if c >= 43 and (p == 3 or p == 5):
        return True
    if c < 43 and p == 3:
        return False
    if c >= 43:
        return False
    else:
        if p % 2 == 0:
            return f(c + 1, p + 1) or f(c + 2, p + 1) or f(c * 2, p + 1)
        else:
            return f(c + 1, p + 1) and f(c + 2, p + 1) and f(c * 2, p + 1)

for S in range(1, 42 + 1):
    if f(S, 1):
        print(S)
