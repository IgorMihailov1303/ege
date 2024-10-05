letters = ["А", "К", "Р", "У"]
cnt = 0

for x in letters:
    for y in letters:
        for z in letters:
            for w in letters:
                for u in letters:
                    if cnt < 450:
                        cnt += 1
                        print(x, y, z, w, u, cnt)
