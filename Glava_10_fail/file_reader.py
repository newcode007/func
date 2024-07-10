filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string=''
for line in lines:
    pi_string += line.strip()

birthday = input("Введите дату, месяц и год своего рождения без пробелов")
if birthday in pi_string:
    print("Моя дата рождения присутствует в число пи")
else:
    print("Моя дата рождения отсутсвует в число пи")

