a = 1
b = 6
for i in range(1000,9999+1):
    i = str(i)
    c = list(map(int, i))
    if ((c[0] + c[1] == a and c[0] + c[1] != b) or (c[0] + c[1] == b and c[0] + c[1] != a)) and ((c[2] + c[3] == a and c[2] + c[3] != b) or (c[2] + c[3] == b and c[2] + c[3] != a)):
        print(i)