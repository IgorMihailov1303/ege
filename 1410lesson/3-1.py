s = sorted(['К','О','М','П','Ь','Т','Е', 'Р'])
x = []
n = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    r = a1+a2+a3+a4+a5
                    n += 1
                    if r.count('К') == 0 and r.count('Р') == 2:
                        x.append(r)
                        print(n)
print(x[-1:])
