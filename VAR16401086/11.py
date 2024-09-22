def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def lensum(n):
    n = list(map(int, n))
    s = sum(n)
    return s

for i in range(70, 200):
    a = "0" + i*'1' + i*'2' + "0"
    while "00" not in a:
        a = a.replace("02", "101", 1)
        a = a.replace("11", "2", 1)
        a = a.replace("12", "21", 1)
        a = a.replace("010", "00", 1)
        if IsPrime(lensum(a)) == True:
            print(i, a)