s = sorted('АЛГОРИТМ')
cnt = 0
for a1 in s:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                r = a1+a2+a3+a4
                cnt += 1
                if r[:2] == 'ИГ':
                    print(r, cnt)
                    break
