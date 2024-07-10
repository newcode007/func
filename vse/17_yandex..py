f = open('17.txt')
a = [int(i) for i in f]
for i in range(len(a)-2):
   sum=0
   stt=[]
   mx=0
   for j in range(i,i+3):
       if 2<=len(str(a[j]))<=3:
           stt.append(a[j])

   if len(stt) == 3:
       print(stt)




