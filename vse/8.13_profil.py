def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

def build_prof(name_user,surname,**user_info):
    prof={}
    prof['name_user'] = name_user
    prof['surname'] = surname
    for key, value in user_info.items():
        prof[key]=value
    return prof


user_profile = build_profile('albert', 'einstein', location = 'princenton', field = 'phisics', cl = '9b')
print(user_profile)

name_surname =  build_prof('Ivan', 'Tyrkin', leaters = '29 let')
print(name_surname)

