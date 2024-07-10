from itertools import *
def delit(x):
    a=[]
    for i in range (1, x+1):
        if x%i==0:
            a.append(i)
    return a

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

c=0
for x in range(670000,10**6+1):
    a = []
    a = delit(x)


    s = 0
    for i in a:
        if is_prime(i) == 1:

            s += i
    if s%10 == 5:
        print(x, s)
        c+=1
    if c==5:
        break



