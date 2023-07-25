from data import MENU, resources


def cash_check(variety):
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))
    value = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)

    if value >= MENU[variety]["cost"]:
        if value > MENU[variety]["cost"]:
            change = round(value - MENU[variety]["cost"], 2)
            print("Here is the $" + str(change) + " in change.")
        return True

    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False


def resource_check(variety):
    if MENU[variety]["ingredients"]["water"] <= resources["water"] and MENU[variety]["ingredients"]["milk"] < resources[
        "milk"] and MENU[variety]["ingredients"]["coffee"] <= resources["coffee"]:
        resources["water"] -= MENU[variety]["ingredients"]["water"]
        resources["milk"] -= MENU[variety]["ingredients"]["milk"]
        resources["coffee"] -= MENU[variety]["ingredients"]["coffee"]
        return True
    else:
        print("Sorry but there is not enough resources")
        return False


while True:
    flavour = str(input("What would you like? (espresso/latte/cappuccino): "))
    flavour = flavour.lower()

    if flavour == "off":
        exit()

    else:
        if flavour == "report":
            print("Water: " + str(resources["water"]))
            print("Milk: " + str(resources["milk"]))
            print("Coffee: " + str(resources["coffee"]))

        else:
            if resource_check(flavour) and cash_check(flavour):
                print("Here is the drink! Enjoy")
