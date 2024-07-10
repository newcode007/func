a= input("Введите свое имя: ")
with open('guest.txt', 'a') as file_jbject:
    file_jbject.write(a)
