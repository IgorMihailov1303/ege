from itertools import *
for x in product("ABC", repeat=2):
    print(x)     #все варианты из двух элементов множества

for x in product("ABC", "DEG"):
    print(x)      #первый элемент из первого множества - второй из второго