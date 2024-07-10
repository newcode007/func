f='guest_book.txt'
name1='1'
name='Guest boxx!'
while name1!='':
    print(name)
    name=input("Как Вас зовут?")
    name1=name
    with open(f,'a') as name_object:
        name = "Добро пожаловать в нашем ресторане, " + name + '!'
        name_object.write(name)
        name_object.write('\n')

