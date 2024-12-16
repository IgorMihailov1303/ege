letters = sorted('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for x in letters:
    for y in letters:
        a = int(f'8{x}78{y}', 13)
        b = int(f'79{x}{y}7', 13)
        print((a+b) / 9)