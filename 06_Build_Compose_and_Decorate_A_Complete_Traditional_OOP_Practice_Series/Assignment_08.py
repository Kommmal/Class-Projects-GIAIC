class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Miss Sana", "Mathematics")

print("Name:", teacher.name)
print("Subject:", teacher.subject)