for A in range(0,1000):
    A_podoshel = True
    for x in range(0,1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)
        break






