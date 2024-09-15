r = 0
c = 0
while r < 100:
    c += 1
    N = bin(c)[2:]

    l = list(map(int, str(N)))
    N2 = N + str(sum(l)%2)

    l2 = list(map(int, str(N2)))
    N3 = N2 + str(sum(l2)%2)

    r = int(N3, 2)
    print(r)