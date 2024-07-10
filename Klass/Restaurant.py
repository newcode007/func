class Restaurant():
    """Класс ресторан"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name, cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self):
        """количество посетителей"""
        print("Количество посетителей: " + str(self.number_served))

    def describe_restaurant(self):
        """Вывод атрибутов"""
        print(self.restaurant_name.title()+" premium restaurant.")
        print(self.cuisine_type.title()+ " cuisine is the most delicious and diverse.")

    def open_restaurant(self):
        """Ресторан открыт"""
        print(self.restaurant_name.title() + " open")

    def increment_number_served(self, number_of_visitors):
        """Изменение количества посетителей"""
        self.number_served+=number_of_visitors





my_restaurant1 = Restaurant("bulki","russian")
my_restaurant2 = Restaurant("vilki","usa")
my_restaurant3 = Restaurant("bulki","yar")
my_restaurant1.describe_restaurant()
my_restaurant2.describe_restaurant()
my_restaurant3.describe_restaurant()
my_restaurant1.set_number_served()
my_restaurant1.increment_number_served(0)
my_restaurant1.increment_number_served(650)
my_restaurant1.set_number_served( )
