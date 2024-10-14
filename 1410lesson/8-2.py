from itertools import *

s1 = 'XYZ'
s2 = 'ABCD'
r = list(product(s1, s2, s2, s2))
print(len(r))
