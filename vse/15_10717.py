def Treug(n, m, k):
    if (n+m > k) and (m+k > n) and (n+k > m):
        return True
    return False

def Mx(a,b):
    if a>b:
        return a
    else:
        return b

for A in range(1,100):
    for x in range(1,1000):
        if not( (Treug(x,11,18) == ((not(Mx(x,5)>68)) )) and Treug(x,A,5)) == False:
            break
    else:
        print(A)
