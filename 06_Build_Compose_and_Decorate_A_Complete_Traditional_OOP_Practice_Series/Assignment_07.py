class Employee:

    def __init__(self, name, _salary, __ssn):

        self.name = name
        self._salary = _salary
        self.__ssn = __ssn

employee1 = Employee("Alice", 50000, "123-45-6789")

# Accessing Public Variable
print("Public (name):", employee1.name)  #  Works

# Accessing Protected Variable
print("Protected (_salary):", employee1._salary)  #  Works


# Accessing Private Variable 
print("Private (__ssn via name mangling):", employee1.__ssn)  # raise AttributeError