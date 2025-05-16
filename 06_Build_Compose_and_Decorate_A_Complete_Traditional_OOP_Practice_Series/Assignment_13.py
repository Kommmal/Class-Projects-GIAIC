class Engine:
    def start(self):
        print("Engine starting")

class Car:
    def __init__(self):
        self.engine = Engine() 

    def start_car(self):
        self.engine.start()

e = Engine()
c = Car()

c.start_car()