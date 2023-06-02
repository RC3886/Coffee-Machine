import time


class CoffeeMaker:
    def __init__(self):  # ingredients units
        self.coffee = 100
        self.water = 100
        self.milk = 100
        self.chocolate = 100
        self.cups = 100

    def ingredients_check(self):
        if self.coffee < 1 or self.water < 1 or self.cups < 1:  # every product needs water, coffee and a cup
            print("This coffee maker is out of order. Sorry for the inconvenience.")
            # future update, add mail to a maintenance stuff

    payment_completed = False           # used to track if payment is completed

    def payment(self, price):
        # 10c, 20c, 50c, 1€, 2€
        while True:
            try:
                print("Please enter the value of the product in coins (10c, 20c, 50c, 1€, 2€).")
                ten_cent = int(input("How many 10 cent coins you want to insert?")) * 10
                twenty_cent = int(input("How many 20 cent coins you want to insert?")) * 20
                fifty_cent = int(input("How many 50 cent coins you want to insert?")) * 50
                one_euro = int(input("How many 1 Euro coins you want to insert?")) * 100
                two_euro = int(input("How many 2 Euro coins you want to insert?")) * 200

                # calculating the entered amount
                entered_amount = ten_cent + twenty_cent + fifty_cent + one_euro + two_euro
                # checking if the price is paid
                if entered_amount == 0:         # an option to not pay and cancel the order
                    self.payment_completed = False
                    break
                elif entered_amount == price:
                    print("Thank you for the payment.")
                    self.payment_completed = True
                    break
                elif entered_amount < price:
                    print("Not enough funds. Please repeat the process.")
                    print(f"Returning {entered_amount / 100} Euro")
                elif entered_amount > price:
                    self.payment_completed = True
                    if entered_amount - price < 100:
                        print(f"Returning {entered_amount - price} cents.")
                        break
                    elif entered_amount - price > 100:
                        print(f"Returning {(entered_amount - price) / 100} Euro.")
                        break
            except ValueError:
                print("Incorrect amount.")

    def preparation(self):
        print("The product is being prepared. Please wait...")
        time.sleep(3)
        print()
        print("The product is ready. Have a nice day!")
        print(" ((")
        print("   ))")
        print("........")
        print("\\      /")
        print(" `----'")
        time.sleep(1.5)

    def cappuccino(self):  # price in cents
        if self.milk < 2:
            print("Not enough ingredients. Please a choose different product.")
        else:
            self.coffee -= 1
            self.milk -= 2  # foam
            self.cups -= 1
            self.water -= 1
            self.preparation()

    def americano(self):
        if self.coffee < 2 or self.water < 2:
            print("Not enough ingredients. Please a choose different product.")
        else:
            self.coffee -= 2
            self.water -= 2  # extra unit of water
            self.cups -= 1
            self.preparation()

    def espresso(self):
        self.coffee -= 1
        self.cups -= 1
        self.water -= 1
        self.preparation()

    def macchiato(self):
        if self.milk < 2:
            print("Not enough ingredients. Please choose a different product.")
        else:
            self.coffee -= 1
            self.milk -= 2  # milk foam
            self.cups -= 1
            self.water -= 1
            self.preparation()

    def mocha(self):
        if self.coffee < 2 or self.chocolate < 1:
            print("Not enough ingredients. Please choose a different product.")
        else:
            self.coffee -= 2
            self.chocolate -= 1
            self.milk -= 1
            self.cups -= 1
            self.water -= 1
            self.preparation()

    def latte(self):
        if self.milk < 2:
            print("Not enough ingredients. Please choose a different product.")
        else:
            self.coffee -= 1
            self.milk -= 2  # milk foam
            self.cups -= 1
            self.water -= 1
            self.preparation()

    def status_check(self):  # an option to check the current status of resources
        print(f"The remaining units of coffe: {self.coffee}/100")
        print(f"The remaining units of water: {self.water}/100")
        print(f"The remaining units of milk: {self.milk}/100")
        print(f"The remaining units of chocolate: {self.chocolate}/100")
        print(f"The remaining units of cups: {self.cups}/100")

    def fill_water(self, amount):
        self.water += amount
        print("Water filled.")

    def fill_coffee(self, amount):
        self.coffee += amount
        print("Coffee filled.")

    def fill_milk(self, amount):
        self.milk += amount
        print("Milk filled.")

    def fill_chocolate(self, amount):
        self.chocolate += amount
        print("Chocolate filled.")

    def fill_cups(self, amount):
        self.cups += amount
        print("Cups filled.")

    def maintenance_mode(self):
        maintenance_enabled = True
        while maintenance_enabled:
            print("Please select the resource you want to fill and press the corresponding button.")
            print("Resource check......0")
            print("Water...............1")
            print("Coffee..............2")
            print("Milk................3")
            print("Chocolate...........4")
            print("Cups................5")
            print("Back................6")

            try:
                maintenance_choice = int(input())
                if maintenance_choice == 0:
                    self.status_check()
                elif maintenance_choice == 1:
                    amount = int(input("Enter the amount of water to fill: "))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive value.")
                    elif self.water + amount > 100:
                        print("Cannot exceed maximum limit of 100 units. Please enter a lower amount.")
                    else:
                        self.fill_water(amount)
                elif maintenance_choice == 2:
                    amount = int(input("Enter the amount of coffee to fill: "))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive value.")
                    elif self.coffee + amount > 100:
                        print("Cannot exceed maximum limit of 100 units. Please enter a lower amount.")
                    else:
                        self.fill_coffee(amount)
                elif maintenance_choice == 3:
                    amount = int(input("Enter the amount of milk to fill: "))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive value.")
                    elif self.milk + amount > 100:
                        print("Cannot exceed maximum limit of 100 units. Please enter a lower amount.")
                    else:
                        self.fill_milk(amount)
                elif maintenance_choice == 4:
                    amount = int(input("Enter the amount of chocolate to fill: "))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive value.")
                    elif self.chocolate + amount > 100:
                        print("Cannot exceed maximum limit of 100 units. Please enter a lower amount.")
                    else:
                        self.fill_chocolate(amount)
                elif maintenance_choice == 5:
                    amount = int(input("Enter the number of cups to fill: "))
                    if amount < 0:
                        print("Invalid amount. Please enter a positive value.")
                    elif self.cups + amount > 100:
                        print("Cannot exceed maximum limit of 100 units. Please enter a lower amount.")
                    else:
                        self.fill_cups(amount)
                elif maintenance_choice == 6:
                    print("Exiting maintenance mode.")
                    maintenance_enabled = False
                else:
                    print("Invalid input. Please select the correct input.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
