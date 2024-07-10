for A in range(1,1000):
    for x in range(1,1000):
        if (((x&123!=0) or  (x & 98 != 0 )) <= ((x & 75 == 0) <= (x & A !=0) ))== False:
            break
    else:
        print(A)
        break


