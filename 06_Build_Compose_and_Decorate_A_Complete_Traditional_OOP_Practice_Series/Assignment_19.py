class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, input):
        print(self.factor * input)

fac1 = Multiplier(3)
print(callable(fac1))
fac1(3)
