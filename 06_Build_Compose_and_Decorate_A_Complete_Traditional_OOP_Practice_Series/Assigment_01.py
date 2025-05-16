class Students:

    def __init__(self, name: str, marks:float):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} \nMarks: {self.marks}")


student1 = Students("Komal", 88)
student1.display()