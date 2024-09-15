# А - 0, В - 1, Т - 2, О - 3, Р - 4, ТАРА - 2040

from string import ascii_lowercase

def tofive(num):
    base = 5
    letters = '0123456789' + ascii_lowercase
    new = ''
    while num > 0:
        num, remainder = divmod(num, base)
        new = letters[remainder] + new
    return new
num = 0
while True:
    if tofive(num) == '2040':
        print(num, tofive(num))
        break
    else:
        print('-',num, tofive(num))
        num += 1
