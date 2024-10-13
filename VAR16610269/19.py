import sys
sys.setrecursionlimit(9999999)

def F(n):
    if n < 11:
        return 10
    else:
        return n + F(n - 1)
print(F(2204) - F(2202))