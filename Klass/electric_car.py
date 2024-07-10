class Car():
    '''Простая модель автомобиля.'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometr(self):
        print('This car has ' + str(self.odometr_reading) + ' miles on it.')

    def update_odometr(self,mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print('You can`t roll back an odometr!')

    def increment_odometr(self, miles):
        self.odometr_reading +=miles

class ElectricCar(Car):
    '''Представляет аспект машины, специфические для электромобилей.'''

    def __init__(self, make, model, year):
        """"Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    #def describe_battery(self):
     #   '''Выводит информацию о мощности аккумулятора'''
     #   print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    #def fill_gas_tank(self):
    #    '''У элктромобилейнет нет бензобака.'''
    #    print('This car doesn`t need a gas tank!')

class Battery():
    """Простая модель аккумулятра электромобиля."""

    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print('This car has a ' + str(self.battery_size)+ "-kWh battery.")

    def get_range(self):
        '''Выводит приблизительный запас хода для аккумулятора.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go appoximately " + str(range)
        message += " meles on a full charge."
        print(message)



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()