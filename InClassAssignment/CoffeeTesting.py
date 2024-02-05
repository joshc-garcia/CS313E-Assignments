class RegularCoffee:
    def __init__(self, price = 1.10, sugar = 0, milk = 0):
        self.price = price
        self.sugar = sugar
        self.milk = milk

    def change_sugar(self, sugar_amount):
        self.sugar = sugar_amount

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
    
class Sugar:
    def change_sugar(self):
        sugar_amount = int(input("How much sugar (0-3)? "))
        if 0 <= sugar_amount <= 3:
            return sugar_amount
        else:
            print("Invalid amount of sugar! Setting sugar to 0.")
            sugar_amount = 0
            return sugar_amount

#############################################################################

class Milk:
    def change_milk(self):
        milk_amount = int(input("How much milk (0-3)? "))
        if 0 <= milk_amount <= 3:
            return milk_amount
        else:
            print("Invalid amount of milk! Setting milk to 0.")
            milk_amount = 0
            return milk_amount

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
            coffee.change_sugar(sugar.change_sugar())

            milk = Milk()
            coffee.change_milk(milk.change_milk())

            coffee.get_price()
            print(coffee)
        elif coffee == "espresso":
            espresso = Espresso()

            sugar = Sugar()
            espresso.change_sugar(sugar.change_sugar())

            milk = Milk()
            espresso.change_milk(milk.change_milk())

            espresso.get_price()
            print(espresso)
        elif coffee == "cappuccino":
            cappuccino = Cappuccino()

            sugar = Sugar()
            cappuccino.change_sugar(sugar.change_sugar())

            cappuccino.get_price()
            print(cappuccino)
        else:
            print("We only offer regular coffee, cappuccino, and espresso!")

if __name__ == "__main__":
    main()