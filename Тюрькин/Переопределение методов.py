class Parent:  # объявите родительский класс
    def my_method(self):
        print('Вызов родительского метода')


class Child(Parent):  # объявите класс наследник
    def my_method(self):
        print('Вызов метода наследника')


c = Child()  # экземпляр класса Child
c.my_method()  # метод переопределен классом наследником

