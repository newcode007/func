for A in range(0,10000):
    for x in range(-100,1000):
        for y in range(-100, 1000):
            if ((x+2*y<A) or (y > x) or (x>60)) == False:
                break
        if ((x + 2*y < A) or (y > x) or (x > 60)) == False:
            break
    else:
        print(A)
        break
