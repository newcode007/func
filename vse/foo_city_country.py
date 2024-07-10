def city_country(city_name, country_name):
    """Город страна с бесконечным циклом"""
    full_name = city_name+', '+country_name
    return full_name.title()

while True:
    print("\nPlease tell me city and country:")
    print("(enter 'q' at any time to quit)")

    f_name=input('City_name: ')
    if f_name=='q':
        break
    c_name = input('City_name: ')
    if c_name == 'q':
        break

    formatted_name=city_country(f_name,c_name)
    print(formatted_name)