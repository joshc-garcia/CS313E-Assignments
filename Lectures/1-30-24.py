"""1/30/2024"""

def my_func(**kwargs):
    """ doc string for documentation """
    age = kwargs.get('age', 0)
    height = kwargs.get('height', 0)

    print(age, height)

    return age

# if __name__ == "__main__":    
    
#     x = my_func(age = 20, height = 7)
#     x1 = my_func(age = 20)
#     x2 = my_func(height = 7, age = 20)
#     x3 = my_func(height = 7)

# Object Oriented Programming
    
"""Example of OOP"""
class Car:
    """This class represents a car"""
    def __init__(self, *args):
        """This is the constructor"""
        self.color = args[0]
        self.price = args[1]
    
    def set_build(self, build):
        if build >= 2000:
            self.build = build
        else:
            self.build = None
            print("The build value is not valid.")

    def calculate_price(self, rate):
        """This method calculates the price"""
        return int(self.price * rate * (self.build - 2000))

##############################################

class Truck(Car):
    def __init__(self, *args):
        # super().__init__(color, price)
        Car.__init__(self, args[0], args[1])
        self.load = args[3]
    
    def max_load(self, load_rate):
        return self.load * load_rate

##############################################
    
class Truck(Car):
    def __init__(self, color, price, load):
        super().__init__(color, price)
        self.load = load
    
    def max_load(self, load_rate):
        return self.load * load_rate

##############################################

        
def main():
    """This is a main function"""
    my_car1 = Car("White", 25000)
    my_car1.set_build(2020)

    final_price = my_car1.calculate_price(1.1)

    my_truck = Truck("Red", 20000, 30000)
    my_truck.set_build(2020)

if __name__ == "__main__":
    main()