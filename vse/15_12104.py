P = list(range(56,79+1))
Q = list(range(63, 85+1))
a=[]
for x in range(0,100):
    if ((not ((x in P) <=(x in Q))) <= ((not (x in Q)) <= (x in a))) == False:
        a.append(x)
print(a)
print(63-56)