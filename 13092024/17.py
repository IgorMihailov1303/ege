file = open('17.txt')
a = [int(x) for x in file]
file.close()

min5 = 0
for x in a:
    if x % 10 == 5 and x < min5:
        min5 = x
print(min5)

cnt = 0
sm = []
for i in range(len(a) - 1):
    if (((a[i] < a [i+1]) and a[i] % 10 == 5) or ((a[i] > a [i+1]) and a[i+1] % 10 == 5)) and (a[i]**2 + a[i+1]**2 < min5**2):
        cnt += 1
        sm.append(a[i]**2 + a[i+1]**2)
print(cnt, max(sm))