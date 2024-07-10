def Mod(m,n):
    return m%n

for A in range(1, 100000):
    for x in range(1,100000):
        if ((A+x) > (700 - A) and ((Mod(A,100)) + (Mod(100,x))) > 50) == False:
            break
    else:
        print(A)
        break
