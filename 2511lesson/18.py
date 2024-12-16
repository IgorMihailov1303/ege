l = []
with open('18') as f:
    for s in f:
        s = s.strip()
        s = float(s.replace(',', '.', 1))
        l.append(s)
print(l)

summ = []
check = []
for i in range(0, len(l)-1):
    for j in range(i, len(l)-1):
        check.append(l[j])
        if abs(l[1+j]-l[j]) > 8:
            summ.append(sum(check))
            check.clear()
            break

print(max(summ))






