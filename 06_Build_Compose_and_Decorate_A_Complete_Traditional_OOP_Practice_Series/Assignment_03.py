class Car:

    def __init__(self, brand: str):
        self.brand = brand

    def start(self):
        print(f"{self.brand}  starting")

car1 = Car("Honda")
car1.start()