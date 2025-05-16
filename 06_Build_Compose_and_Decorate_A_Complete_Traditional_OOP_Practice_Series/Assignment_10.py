class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} breed is {self.breed}")

dog1 = Dog("Candy", "Golden Retriever")
dog1.bark()
