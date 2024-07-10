from fnmatch import *
for a in range (98591,10**12,98591):
    if fnmatch(str(a), '12?3*456??9'):
        print(a, a//98591)
