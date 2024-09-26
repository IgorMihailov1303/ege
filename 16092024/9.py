text = open('9.txt')

cnt = 0
for i in text:
    tl = [int(j) for j in i.split()]
    d = tl.sort()
    if len(set(tl)) < len(tl) and tl.count(tl[5]) == 1 and (sum(tl) - sum(set(tl)))*2 < tl[5]:
        cnt += 1
print(cnt)