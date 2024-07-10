def Del1(n, m):
    return n% m == 0
for A in range(1, 1000000):
    A_podoshel = True
    for x in range(1, 1000000):
        if ((not(Del1(x,A))) <= (Del1(x,6) <= (not(Del1(x,9))))) == False:
            A_podoshel = False
            break
    if A_podoshel == True:
        print(A)

