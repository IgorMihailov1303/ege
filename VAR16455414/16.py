for A in range(100):
    a = 0
    for n in range(100):
        for m in range(100):
            if (3 * m + 4 * n > 63) or ((m <= A) or (n < A)):
                a += 1
    if a == 10000:
        print(A)
        break