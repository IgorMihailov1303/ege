r = 0
n = 0
while r < 102:
    b = str(bin(n))[2:]
    if n % 2 == 0:
        b += "10"
    else: b += "01"
    r = int(b, 2)
    print(r)
    n += 1
