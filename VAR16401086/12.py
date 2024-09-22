a = 78*'1'
while '111' in a:
    a = a.replace('111', '2', 1)
    a = a.replace('222', '11', 1)
    print(a)
