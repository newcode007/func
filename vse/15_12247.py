for A in range(1,1000):
    for x in range(0,1000):
        for y in range(0, 1000):
            if ((x & A ==0) or (not(x & 37 == 0)) or (not (x & 12 == 0))) == False:
                break
        if ((x & A == 0) or (not (x & 37 == 0)) or (not (x & 12 == 0))) == False:
            break
    else:
        print(A)