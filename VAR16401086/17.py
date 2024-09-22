file = open('17.txt')
a = [int(x) for x in file]
file.close()

r = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        c = a[i] + a[j]
        if c % 80 == 0 and (a[i] % 50 == 0 or a[j] % 50 == 0):
            #print(a[i], a[j])
            r.append(c)
print(len(r), max(r))