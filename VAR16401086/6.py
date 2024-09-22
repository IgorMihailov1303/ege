a = 6
b = 16
cnt = 0
for i in range(1000,9999+1):
    i = str(i)
    c = list(map(int, i))
    if (c[0] + c[1] == a and c[2] + c[3] == b) or (c[0] + c[1] == b and c[2] + c[3] == a):
        cnt += 1
        print(i, cnt)