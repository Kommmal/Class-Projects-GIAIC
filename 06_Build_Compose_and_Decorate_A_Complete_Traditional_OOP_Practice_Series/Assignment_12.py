class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
       return (c * 9.0)/5.0 + 32
    
temp1 = TemperatureConverter()
print(temp1.celsius_to_fahrenheit(30))