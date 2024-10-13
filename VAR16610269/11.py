cnt = 0
for txt in open('11'):
    n = list(map(int, txt.split()))
    mx = max(n)
    s_nmx = sum(n) - mx
    if mx < s_nmx and len(set(n)) == 4:
        cnt += 1
print(cnt)
