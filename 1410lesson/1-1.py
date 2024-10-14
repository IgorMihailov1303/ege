from string import ascii_lowercase
#К-0 Л-1 Р-2 Т-3

def tofour(num):
    base = 4
    letters = '0123456789' + ascii_lowercase
    new = ''
    while num > 0:
        num, remainder = divmod(num, base)
        new = letters[remainder] + new
    return new
num = 0
while True:
    if num == 67-1:
        print(num, tofour(num))
        break
    else:
        print('-',num, tofour(num))
        num += 1
#1002 - Л К К Р