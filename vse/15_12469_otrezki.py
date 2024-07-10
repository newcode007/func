D = list(range(7,68+1))
C = list(range(29,100+1))
a = []
for x in range(0,120):
    if ((x in D) <= (((not (x in C)) and (not(x in a))) <= (not(x in D)))) == False:
        a.append(x)
print(a)

print(29-7)