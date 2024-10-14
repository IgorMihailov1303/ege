from itertools import *

s = sorted('КЛРТ')

m = [0] + list(product(s, repeat=4))
print(m[67])