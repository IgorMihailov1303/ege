for i in range(100):
    for j in range(100):
        for l in range(100):
            a = "0" + "1"*i + "2"*j + "3"*l

            while ("01" in a) or ("02" in a) or ("03" in a):
                a = a.replace("01", "2302", 1)
                a = a.replace("02", "10", 1)
                a = a.replace("03", "201", 1)

                if a.count('1') == 40 and a.count('2') == 10 and a.count('3') == 8:
                    print(i, j, l, a)

#много различных вариантов, незнаю какой именно нужен, как отсеить лишние
