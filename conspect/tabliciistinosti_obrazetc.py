from itertools import *
def Usl(x, y, z, w):
    pass #Условие

for a1, a2, a3, a4, a5, a6, an in product([1,0], repeat=7):   #в пропущенные клетки подставляем все возможные комбинации единиц и нулей
    tab = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, an, 1)]   #заполняем таблицу
    if len(tab) == len(set(tab)):                       #проверяем, все ли строки у нас разные
        for p in permutations('xyzw'):
            if [Usl(**dict(zip(p,r))) for r in tab] == [0,0,0]:
#                            |подставляем все P ко всем в Tab  |проверяем равенство условию
                print(p)

