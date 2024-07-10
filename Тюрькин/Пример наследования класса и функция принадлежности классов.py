class Parent:  # объявляем родительский класс
    parent_attr = 100

    def __init__(self):
        print('Вызов родительского конструктора')

    def parent_method(self):
        print('Вызов родительского метода')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print('Атрибут родителя: {}'.format(Parent.parent_attr))


class Child(Parent):  # объявляем класс наследник
    def __init__(self):
        print('Вызов конструктора класса наследника')

    def child_method(self):
        print('Вызов метода класса наследника')

print(issubclass(Child, Parent)) #для проверки отношений двух классов и экземпляров. первое - подкласс(наследник) второе класс(родитель) тогда истина



c = Child()  # экземпляр класса Child
c.child_method()  # вызов метода child_method
c.parent_method()  # вызов родительского метода parent_method
c.set_attr(200)  # еще раз вызов родительского метода
c.get_attr()  # снова вызов родительского метода