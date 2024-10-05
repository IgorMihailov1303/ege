letters = sorted('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for x in letters:
    for y in letters:
        a = int(f'{x}341{y}', 11)
        b = int(f'56{x}1{y}', 19)
        print((a+b) / 305)
