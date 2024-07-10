class User():
    """Класс на first_name и last_name"""

    def __init__(self, first_name, last_name, age, education, login_attempts):
        """Инициализиуер атрибуты first_name, last_name, age, education """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.education = education
        self.login_attempts = login_attempts

    def describe_user(self):
        """Сводка с информацией о пользователе"""
        print("First_name: " + self.first_name.title())
        print("Last_name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Education: " + self.education.title())
        print("Login_attempts: " + str(self.login_attempts))

    def greet_user(self):
        """Персональное приветствие"""
        print("Hello, " + self.first_name.title()+' '+ self.last_name.title()+'!')

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts =  0





user_name1 = User('ivan', 'tyrkin', 29, 'higher', 0)
user_name2 = User('pety', 'petrov', 25, 'secondary', 0)
user_name1.describe_user()
user_name1.greet_user()
print()
user_name2.increment_login_attempts()
user_name2.increment_login_attempts()
user_name2.increment_login_attempts()

user_name2.describe_user()
user_name2.greet_user()
user_name2.reset_login_attempts()
print(user_name2.login_attempts)



