def f(n):
    n2 = bin(n)[2:]
    n2 = n2[:-1]
    if n%2 == 1:
        n2 = n2 + '10'
    else:
        n2 = n2 + '01'
    return int(n2, 2)

for N in range(2, 100001):
    if f(N) == 2018:
        print(N)
