class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__("Age must be greater than 18")
        self.age = age

class Age:
    def check_age(self, age):
        if age < 18:
            raise InvalidAgeError(age)
        else:
            print("Your age is valid")
        
age = Age()

try:
    age.check_age(16)
except InvalidAgeError as e:
    print(e)
