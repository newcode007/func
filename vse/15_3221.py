def fak(A,x):
    return (((x%3==0) <= ((not(x%5==0)))) or (x+A>=70))



for A in range(1,1000):
    for x in range (1,10000):
        if all(fak(A,x)) == True:
            print(A)