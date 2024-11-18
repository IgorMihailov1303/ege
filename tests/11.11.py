d1 = []
d2 = []
d0 = []

k=[[],[],[]]
# i=7
# k[i%3].append(i)
# max(k[1])

with open('27-B.txt') as f:
    for s in f:
        s = int(s)
        k[s%3].append(s)

k[0] = sorted(k[0])
k[1] = sorted(k[1])
k[2] = sorted(k[2])

s111 = k[1][0] + k[1][1] + k[1][2]
s000 = k[0][0] + k[0][1] + k[0][2]
s120 = k[1][0] + k[2][0] + k[0][0]
s222 = k[2][0] + k[2][1] + k[2][2]
print(min(s222, s111, s000, s120))