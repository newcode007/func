from itertools import product
cnt=0
ch='0246'
nch='135'
w = product('0123456', repeat=6)
for s in w:
    c=0
    if s[0]!=0 and s.count('3')==1:
        for i in range(len(s)-1):
            if s[i] in nch and s[i+1]  in nch:
                c+=1
        if c==0:
            cnt+=1
print(cnt)


