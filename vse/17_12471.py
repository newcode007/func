f = open('17_12471.txt')
data =[ int(i) for i in f]
c=0
mx = [int(i) for i in data if int(i)%100==13]
Maximum = max(mx)
summa=[]
for i in range(0,len(data)-2):
    if (((data[i]%2==0 and data[i+1]%2==0 and data[i+2]%2==0) or (99>=data[i]>=10 or 99>=data[i+1]>=10 or 99>=data[i+2]>=10)) and (data[i]+data[i+1]+data[i+2])<=Maximum):
        summa.append(data[i] + data[i + 1] + data[i + 2])
        print(data[i],data[i+1],data[i+2])
        c+=1
        print('------')
print(c,sum(summa)//len(summa))
for x in range(0,10):
    print(x, data.count(x),Maximum)

