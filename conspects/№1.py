from itertools import *

t = '12 14 21 24 26 35 36 41 42 46 47 53 56 62 63 64 65 67 74 76' #все пары в таблице
g = 'АБ АВ БА БВ ВА ВБ ВД ВЕ ВГ ДВ ДЕ ЕД ЕВ ЕГ ЕК ГВ ГЕ ГК КЕ КГ' #все пары на графе

s = set(g.replace(' ', '')) #делаем список из пар графа
for p in permutations(s): #рассматриваем все возможные перестановки пар графа
    nt = t              #нам нужны копии t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)  #заменяем буквы на цифры
    if set(g.split()) == set(nt.split()):
        print(p)