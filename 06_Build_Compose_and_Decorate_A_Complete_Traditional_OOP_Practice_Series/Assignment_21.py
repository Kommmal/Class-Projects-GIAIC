class Countdown:
    def __init__(self, start_num):
        self.start_num = start_num
        
    def __iter__(self):
        self.current_num = self.start_num
        return self
    def __next__(self):
        if self.current_num < 0:
            raise StopIteration
        else:
            num = self.current_num
            self.current_num -= 1
            return num 

cd = Countdown(10)
for number in cd:
    print(number)

