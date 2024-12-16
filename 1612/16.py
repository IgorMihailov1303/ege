import sys
sys.setrecursionlimit(9999)

def F(n):
    if n < 9:
        return n
    else:
        return F(n % 9)+F(n // 9)
cnt = 0
for i in range(4*(6**20),5*(6**20)):
    if F(i) == 121:
        cnt += 1

print(cnt)

