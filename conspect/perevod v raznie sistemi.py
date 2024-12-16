from string import ascii_lowercase

while True:
    num = int(input())
    base = 2
    new = ''
    while num > 0:
        new = str(num%base) + new
        num = num // base
    print(new)

def tofour(num):
    base = 4
    letters = '0123456789' + ascii_lowercase
    new = ''
    while num > 0:
        num, remainder = divmod(num, base)
        new = letters[remainder] + new
    return new
