cnt = 0
for N in range(234567900, 789012345+1):
    l = '1'*N
    while '111' in l:
        l = l.replace('111', '2', 1)
        l = l.replace('222', '11', 1)
        l = l.replace('1', '2', 1)
    if len(l) == 3:
        cnt += 1
print(cnt)