a = [1,2,3,4,5,6,7,8,9]
print(a[2:]) #со второго элемента и далее
print(a[:2]) #до второго элемента
print(a[:-2]) #до второго с конца

a2 = '123456789'
c = list(a2) #разделить на элементы строку
print(c)
c = list(map(int, a2)) #получить числа, а не строку
print(c)

a3 = '12,34,56,78'
c = list(map(int, a3.split(','))) #split делит строку на промежутки с указанными разделителями
print(c)

c = [str(x) for x in a] #делает из массива чисел - строку
print(c)

d = ''
d = ''.join(c) #схлопывает массив из строк в одну строку
print(d)