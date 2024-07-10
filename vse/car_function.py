def make_car(brand, model, **user_info):
    """"Описание автомобиля"""
    car={}
    car['brand']=brand
    car['model']=model
    for key, value in user_info.items():
        car[key]=value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)