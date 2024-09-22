while True:
    num = 9**8 + 3**5 - 2
    base = 3
    new = ''
    while num > 0:
        new = str(num%base) + new
        num = num // base
    print(new)
    break
print(new.count('2'))