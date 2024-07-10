from itertools import *
from fnmatch import*
a=[]
for x in range(5364,10**12,14900):
    if fnmatch(str(x),'1*28?64'):
        a.append(x)
print(len(a),sum(a)//len(a))