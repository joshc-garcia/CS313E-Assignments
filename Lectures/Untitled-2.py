class Car:
    """This class defines a basic car"""

    def __init__(self, cspeed, ngears):
        """
        A Car has a Speed attribute and number of Gears.
        """
        self.speed = cspeed
        self.gears = ngears

    def __str__(self):
        return "This is a car that runs with speed of " + str(self.speed)
    
    def __eq__(self, other):
        return self.speed == other.speed
    
#####################################################

my_car1 = Car(30, 4)
my_car2 = Car(30, 5)

if my_car1 == my_car2:
    print('These are running with the same speed.')
