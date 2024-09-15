from math import floor
def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return floor( (3*n + F(n-3))/3 )
    else:
        return floor( (n*7 + F(n-1) - F(n-2))/5 )
print(F(35))