from itertools import product
a = 0
words = list(product('ЗИМА', repeat=5))
for x in words:
    if x.count('З') + x.count('А') == 1:
        a += 1
print(a)
