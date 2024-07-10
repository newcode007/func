f = open('24.txt').readline()

glasn = 'AEIOUY'
sogl = 'BCDFGHJKLMNPQRSTVWXZ'
stroka=''
a=[]
pr=''
for i in range(len(f)-1):
    stroka+=f[i]
    if f[i]<f[i+1]:
        pr=stroka+f[i+1]
        if (pr.count('A') + pr.count('E')+ pr.count('I') + pr.count('O')+ pr.count('U') + pr.count('Y'))<=1 and len(pr)>8:
            print(pr)
            a.append(len(pr))
    else:
        stroka = ''
print(max(a))















