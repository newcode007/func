P = list(range(5,30+1))
Q = list(range(14,23+1))

A=[]
for x in range(-10,100):
    if ((x in P) == (x in Q) <= (not(x in A))) == False:
        A.append(x)
print(A)
