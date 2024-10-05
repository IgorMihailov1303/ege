a = 25**5 + 5**14 - 5
b = ''
while a > 0:
    b += str(a%5)
    a = a // 5
c = b[::-1]
c = c.strip()
c = list(map(int, str(c)))
print(c.count(4))