class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp1 = Employee("Komal")

dep = Department(emp1)
print(dep.employee.name)