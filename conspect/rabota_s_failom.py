f = open('1.txt') #открыть файл
m = f.readlines() #засовывает все строчки файла в массив

with open('1.txt') as f: #нормальный способ чтения фалов без забивания памяти
    for s in f:          #
        s = s.strip()    #
        print(s)         #

k = 12
s = f"aaaaaaaaaaaaaaaa{k}ssss" #позволяет соединять переменные и строки
print(s)

s = f'{k}' #делает из переменной строку

s = 'asdjfgeopipoajfj'
s = s.replace('a', 'XX', 1) #поменять "а" на "ХХ" N раз (отсчёт c лева на право)
print(s)


s = '9' * 127
while ('333' in s) or ('999' in s):
    if '333' in s:
        s = s.replace('333', '9', 1)
    else:
        s = s.replace('999', '3', 1)
print(s)
