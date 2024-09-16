#Три способа перебора массивов
a = [2, 3, 4, 5, 6, 1, 2, 3]
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

for i,v in enumerate(a): #берет и значение и индекс одновременно
    if v%2 == 0:
       a[i] *= 0
    print(i,v,a)