from resources import CoffeeMaker

coffee_maker = CoffeeMaker()

while True:                                                      # constantly running machine
    try:
        coffee_maker.ingredients_check()
        print("Please select the product from the list bellow and press the the corresponding button.")
        print("1 Cappuccino.....2 €")
        print("2 Americano......2 €")
        print("3 Espresso.......1.50 €")                                         # menu
        print("4 Macchiato......2.50 €")
        print("5 Mocha..........3 €")
        print("6 Latte..........2.50 €")

        customer_choice = int(input())

        if customer_choice == 1:
            coffee_maker.payment(200)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.cappuccino()
        elif customer_choice == 2:
            coffee_maker.payment(200)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.americano()
        elif customer_choice == 3:
            coffee_maker.payment(150)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.espresso()
        elif customer_choice == 4:
            coffee_maker.payment(250)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.macchiato()
        elif customer_choice == 5:
            coffee_maker.payment(300)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.mocha()
        elif customer_choice == 6:
            coffee_maker.payment(250)
            if not coffee_maker.payment_completed:
                print("Order cancelled.")
                continue
            elif coffee_maker.payment_completed:
                coffee_maker.latte()
        elif customer_choice == 3886:                                # adds special maintenance access code
            print("You are entering the maintenance mode.")
            coffee_maker.maintenance_mode()
        else:
            print("Invalid input. Please select the correct input.")

    except ValueError:
        print("Invalid choice. Please enter one of the options from the table.")