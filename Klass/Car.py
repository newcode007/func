class Car():
    """Модель автомобиля."""

    def __init__(self,make, model, year):
        """Инициализиуер атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 250

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year)+ ' ' +self.make + ' '+ self.model
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в километрах."""
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре.
        При попытке скрутки пробега изменение отклоняется"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometr")

    def increment_odometr(self,km):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += km

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometr(100)
my_used_car.read_odometer()
