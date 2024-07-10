f = open('17.txt')

a = [int(i) for i in f]



s=[]
b=[]
c=0
for i in range(len(a)-2):
    stroka = ''
    summa = 0
    Mx = 0
    tri = 0
    if a[i]%100==13 or a[i+1]%100==13 or a[i+2]%100==13:
        stroka=str(a[i])+str(a[i+1])+str(a[i+2])
        if 99<a[i]<1000:
            tri+=1
        if 99<a[i+1]<1000:
            tri+=1
        if 99<a[i+2]<1000:
            tri+=1
        if tri == 2:
            for j in stroka:
                summa+=int(j)
            if Mx<a[i] and a[i]%100==13:
                Mx=a[i]
            if Mx<a[i+1] and a[i+1]%100==13:
                Mx=a[i+1]
            if Mx<a[i+2] and a[i+2]%100==13:
                Mx=a[i+2]
            if tri==2 and summa<=Mx:
                b.append(str(a[i]) + ' '+ str(a[i+1]) + ' '+ str(a[i+2]))
                c+=1
                s.append(summa)



print(b)
print(c,max(s))