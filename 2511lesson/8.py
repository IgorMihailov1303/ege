a = int(input())
cnt = 0
while a != 0:
    a = int(input())
    if a % 2 == 0 and a % 7 == 0:
        cnt += 1
print(cnt - 1)