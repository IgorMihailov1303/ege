m = []
with open("17.txt") as f:
    for s in f:
        s = int(s.strip())
        m.append(s)

cnt = 0
mx = []
for i in range(0, len(m)-1):
    if (m[i]%160) != (m[i+1]):
        if m[i]%7==0 or m[i+1]%7==0:
            cnt += 1
            mx.append(m[i]+m[i+1])

print(cnt, max(mx))