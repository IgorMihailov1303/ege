# А - 0, В - 1, Л - 2, О - 3, Р - 4   ЛААА - 2000

from string import ascii_lowercase

def tofive(num):
    base = 5
    letters = '0123456789' + ascii_lowercase
    new = ''
    while num > 0:
        new = str(num%base) + new
        num = num // base
    return new
num = 0
while True:
    if tofive(num) == '2000':
        print(num, tofive(num))
        break
    else:
        print('-',num, tofive(num))
        num += 1