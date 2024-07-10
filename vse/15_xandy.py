for A in range(1,10000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((2 * x + y != 70) or (x < y) or (A < x)) == False:
                break
        if ((2 * x + y != 70) or (x < y) or (A < x)) == False:
            break
    else:
        print(A)