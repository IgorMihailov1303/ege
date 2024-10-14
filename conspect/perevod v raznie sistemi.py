while True:
    num = int(input())
    base = 5
    new = ''
    while num > 0:
        new = str(num%base) + new
        num = num // base
    print(new)