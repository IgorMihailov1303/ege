a = 125 + 25**3 + 5**9
b = ''
while a > 0:
    b += str(a % 5)
    a = a // 5
c = b[::-1]
c = c.strip()
c = list(map(int, str(c)))
print(c.count(0))