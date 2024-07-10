print('Для выхода из программы введите: quit')
a,b = input('Введите через пробел два числа:').split()
while a!='quit' or b!='quit' or a!='' or b!='' :
    try:
        sum=int(a)+int(b)
    except ValueError:
        print('Ошибка: число является строкой')
    print(sum)
    try:
        a, b = input('Введите через пробел два числа:').split()
    except ValueError:
        a, b = input('Введите через пробел два числа:').split()