class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count=0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count+=1

    def displey_count(self):
        print('Всего сотрудников: %d' % Employee.emp_count)

    def displey_employee(self):
        print('Имя: {}. Зарплата: {}'.format(self.name, self.salary))

emp1 = Employee("Андрей", 2000)
emp2 = Employee("Мария", 5000)


emp1.displey_employee()
emp2.displey_employee()

print("Всего сотрудников: %d" % Employee.emp_count)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)


