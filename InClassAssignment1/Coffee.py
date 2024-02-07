# Student: Joshua Garcia
# Class: CS313E
# UT EID: jcg4725
# Unique Class ID: 50775
# Description: Program that simulates a coffee vending machine that allows
# for the user to choose several different types of coffee.


class RegularCoffee:
    def __init__(self, price = 1.10, sugar = 0, milk = 0):
        self.price = price
        self.sugar = sugar
        self.milk = milk

    def change_milk(self, milk_amount):
        self.milk = milk_amount

    def get_price(self):
        self.price = self.price + (0.10 * self.sugar) + (0.15 * self.milk)
        return self.price

    def __str__(self):
        return "Your coffee costs $" + format((self.price), ".2f") + "."
    
#############################################################################

class Espresso(RegularCoffee):
    def __init__(self, price = 1.10, sugar = 0, milk = 0):
        super().__init__(price, sugar, milk)

    def get_price(self):
        self.price = (1.20 * self.price) + (0.10 * self.sugar) + (0.15 * self.milk)

    def __str__(self):
        return "Your espresso costs $" + format((self.price), ".2f") + "."

#############################################################################
    
class Cappuccino(RegularCoffee):
    def __init__(self, price = 1.10, sugar = 0):
        super().__init__(price, sugar)

    def get_price(self):
        self.price = 1.15 * (1.20 * self.price) + (0.10 * self.sugar)

    def __str__(self):
        return "Your cappuccino costs $" + format((self.price), ".2f") + "."

#############################################################################

class Milk:
    @staticmethod
    def change_milk(coffee_instance):
        milk_amount = int(input("How much milk (0-3)? "))

        if 0 <= milk_amount <= 3:
            coffee_instance.milk = milk_amount
        else:
            print("Invalid amount of milk! Setting milk to 0.")
            coffee_instance.milk = 0

#############################################################################

class Sugar:
    @staticmethod
    def change_sugar(coffee_instance):
        sugar_amount = int(input("How much sugar (0-3)? "))
        
        if 0 <= sugar_amount <= 3:
            coffee_instance.sugar = sugar_amount
        else:
             print("Invalid amount of sugar! Setting sugar to 0.")
             coffee_instance.sugar = 0

#############################################################################
            
def main():
    while True:
        coffee_input = True
        
        print('\nNotice: To exit out, please select the "q" button.')
        coffee = input("What type of coffee would you like (Regular Coffee, Cappuccino, Espresso)? ").lower()

        if coffee == 'q':
            break

        if coffee == "regular coffee":
            coffee = RegularCoffee()

            sugar = Sugar()
            sugar.change_sugar(coffee)

            milk = Milk()
            milk.change_milk(coffee)

            coffee.get_price()
            print(coffee)
        elif coffee == "espresso":
            espresso = Espresso()

            sugar = Sugar()
            sugar.change_sugar(espresso)

            milk = Milk()
            milk.change_milk(espresso)

            espresso.get_price()
            print(espresso)
        elif coffee == "cappuccino":
            cappuccino = Cappuccino()

            sugar = Sugar()
            sugar.change_sugar(cappuccino)

            cappuccino.get_price()
            print(cappuccino)
        else:
            print("We only offer regular coffee, cappuccino, and espresso!")

if __name__ == "__main__":
    main()