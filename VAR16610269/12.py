cnt = 0
for txt in open('12'):
    n = sorted([int(i) for i in txt.split()])
    if len(set(n)) == 5:
        a = sum(n) - sum(set(n))
        if a < (sum(n) - a*2) / 4:
            cnt += 1
print(cnt)
