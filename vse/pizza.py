def make_pizza(size, *toppings):
    """Вывод описание пиццы"""
    print("\nMaking a " +  str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


