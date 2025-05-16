class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, new_price):
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative!")

    @price.deleter
    def price(self):
        print("Delting Price")
        del self._price

product1 = Product(100)
print(product1.price)


product1.price = 50
print(product1.price)

del product1.price 