for n in range(3,10000):
    summa=0
    stroka='5'+n*'2'
    while ('52' in stroka) or ('2222' in stroka) or ('1122' in stroka):
        if ('52' in stroka):
            stroka=stroka.replace('52','11')
        elif '2222' in stroka:
            stroka=stroka.replace('2222','5')
        else:
            stroka=stroka.replace('1122','25')
    for i in stroka:
        summa+=int(i)
    if summa == 64:
        print(n)
