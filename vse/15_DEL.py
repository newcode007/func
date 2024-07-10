def Del(n, m):
    return n%m==0

for A in range(0, 10000):
    for x in range(1, 10000):
        if ((Del(x,2) <= (not(Del(x,3)))) or (x + A>=100)) == False:
            break
    else:
        print(A)
        break

