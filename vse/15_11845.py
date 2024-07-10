def Del(n,m):
    return n%m ==0

c=0
for A in range(1,11111+1):
    for x in range(1, 10**5):
        if (Del(A,x) <= (x==A) or (x == 1)) == False:
            break
    else:
        c+=1
print(c)