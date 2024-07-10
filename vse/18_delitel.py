def Del(n,m):
    if n%m==0:
        return True
    else:
        return False

for A in range(1,10000):
    for x in range(1,10000):
        if ((not (Del(x,A))) <= ((Del(x,6))<=((not(Del(x,4)))))) == False:
            break
    else:
        print(A)