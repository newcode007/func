def sandwicch_components(name_sandwich, **user_info):
    """Список компонентов сэндвича"""
    baton = {}
    baton['name_sandwich']=name_sandwich
    for key, value in user_info.items():
        baton[key] = value
    return baton

given = sandwicch_components('gamberger', price = '`14 cent', size = 'big'  )
print(given)
