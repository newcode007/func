P = list(range(5,54+1))
Q = list(range(50,93+1))
for A in range(-100,100):
    c=0
    for x in range(0, 93+1):
        if ((not (x in P)) and (x in Q) <= (x>A))== False:
            c += 1
    print(A,c)


    if c==20:
        print(A)
        break

