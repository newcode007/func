P = list(range(257,1000+1))
Q = list(range(5,100+1))
R = list(range(99,258+1))
a=[]
for x in range(-100,1001):
    if (((x in a) <= (x in R)) and ((not((x in a) <= (x in P))))) == True:
        a.append((x))
print(a)