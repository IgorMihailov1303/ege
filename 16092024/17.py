text = open('17.txt')
cnt = 0
r = 0

tl = [int(i) for i in text]
for m in range(len(tl) - 1):
    for n in range(m+1, len(tl)):
        if (m + n) % 120 == 0:
            cnt += 1
            r = max(r, m + n)

print(cnt, r)