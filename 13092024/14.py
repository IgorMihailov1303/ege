from string import ascii_lowercase

letters = '0123456789' + ascii_lowercase
for x in letters:
    a1 = int('26' + x + '98', 13)
    a2 = int('4' + x + '296', 13)
    if (a1 + a2) % 34 == 0:
        print(x, (a1 + a2) // 34)
