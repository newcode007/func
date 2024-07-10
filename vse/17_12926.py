f = open('17_12926.txt')
data = [int(i) for i in f]
amax=[]
mx2=[int(i) for i in data if 99>=i>=10]
mx=max(mx2)
h=0
summa5=[]
for i in range(len(data)-3):
    x1=data[i]
    x2=data[i+1]
    x3=data[i+2]
    x4=data[i+3]
    if abs(x1)%10==abs(x2)%10==abs(x3)%10==abs(x4)%10:
        amax.append(x1+x2+x3+x4)
for i in range(len(data)-4):
    x1=data[i]
    x2=data[i+1]
    x3=data[i+2]
    x4=data[i+3]
    x5=data[i+4]
    c=0
    for j in x1,x2,x3,x4,x5:
        if j<max(amax):
            c+=1
    if c==1 and (x1+x2+x3+x4+x5)%mx==0:
        h+=1
        summa5.append(x1+x2+x3+x4+x5)
print(h, min(summa5),max(am)
