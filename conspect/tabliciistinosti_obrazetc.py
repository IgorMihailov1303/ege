from itertools import *
def Usl(x, y, z, w):
    pass #Условие

for a1, a2, a3, a4, a5, a6, an in product([1,0], repeat=7):   #в пропущенные клетки подставляем все возможные комбинации единиц и нулей
    tab = [(1, a1, a2, 1), (1, a3, a4, a5), (a6, 1, an, 1)]   #заполняем таблицу
    if len(tab) == len(set(tab)):                       #проверяем, все ли строки у нас разные
        for p in permutations('xyzw'):
            if [Usl(**dict(zip(p,r))) for r in tab] == [0,0,0]:
#                   |подставляем все P ко всем в Tab  |проверяем равенство условию
                print(p)




def Usl1(x, y, z, w):                              #Этот метод работает и с несколькими условиями сразу, просто в if пишем and и второе условие
    l1 = w == x
    l2 = y <= z
    return l1 and l2
def Usl2(x, y, z, w):
    l1 = w <= x
    l2 = y == z
    return l1 <= l2

for a1, a2, a3, a4, a5 in product([1,0], repeat=5):                                                                     #неизвестные можо ставить и в функции
    tab = [(1 , a1, 1, 1), (a2, 1, 0, 0), (a3, 0, 0, a4)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if ([Usl1(**dict(zip(p,r))) for r in tab] == [1,1,0]) and ([Usl2(**dict(zip(p,r))) for r in tab] == [0,a5,0]):
                print(p)

