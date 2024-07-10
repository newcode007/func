a = []
for i in range(0, 100000):
    n_3 = ''
    sum = 0
    N = i
    troi = ''
    while i != 0:
        troi = str(i % 3) + troi
        i = i // 3
    for i in range(len(troi)):
        sum += int(i)
    i = (sum % 4) * 3
    while i != 0:
        n_3 = str(i % 3) + n_3
        i = i // 3
    if sum % 4 == 0:
        troi = '1' + troi[:-2]
    else:
        troi = troi + n_3
    R = int(troi, 3)
    if R > 353:
        a.append(R)
print(min(a))


