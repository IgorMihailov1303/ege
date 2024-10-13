cnt = 0
for txt in open('10'):
    l = [int(n) for n in txt.split()]
    if len(l) == len(set(l)):
        l1 = [n for n in l if n % 2 == 0]
        l2 = [n for n in l if n % 2 != 0]
        if len(l2) > len(l1):
            if sum(l2) < sum(l1):
                cnt += 1
print(cnt)
