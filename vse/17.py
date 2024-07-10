f =open('17_12926.txt')
a = [int(i) for i in f]
mxsum4=[]
mnsum5=[]
ch=0
count=0
maxim=0
for i in range(len(a)-3):
    if a[i]%10==a[i+1]%10==a[i+2]%10 == a[i+3]%10:
        mxsum4.append([a[i]+a[i+1] + a[i+2] + a[i+3]])

ch1=str(max(mxsum4))[1:-1]

print(a[2]%10)
