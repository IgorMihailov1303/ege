l = []
summ = []
with open('17 (1).txt') as f:
    for s in f:
        s = int(s.strip())
        l.append(s)
#
# for i in range(0, len(l)):
#     for j in range(0, len(l)):
#         if i >= j:
#             if ((l[i]+l[j])%2 == 1) and (l[i]*l[j])%5 == 0:
#                 summ.append(l[i]+l[j])
# print(max(summ), len(summ))


nch = []
ch = []
nch5 = []
ch5 = []
for i in range(0, len(l)):
    if l[i] % 2 == 0:
        if l[i] % 5 == 0:
            ch5.append(l[i])
        else:
            ch.append(l[i])
    elif l[i] % 2 == 1:
        if l[i] % 5 == 0:
            nch5.append(l[i])
        else:
            nch.append(l[i])

s1 = []
s2 = []
s3 = []
for i in range(0, len(ch5)):
    for j in range(0, len(nch5)):
                s1.append(ch5[i]+nch5[j])
for i in range(0, len(ch)):
    for j in range(0, len(nch5)):
                s2.append(ch[i]+nch5[j])
for i in range(0, len(ch5)):
    for j in range(0, len(nch)):
                s3.append(ch5[i]+nch[j])

print(max(s1), max(s2), max(s3), len(s1)+len(s2)+len(s3))

