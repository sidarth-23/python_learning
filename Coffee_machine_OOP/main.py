import self as self

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


check = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while check:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}):")

    if choice == "off":
        exit()

    elif choice == "report":
        coffee_maker.report()

    else:
        choice_check = menu.find_drink(choice)
        if choice_check is None:
            break
        else:
            resource_check = coffee_maker.is_resource_sufficient(choice_check)
            if not resource_check:
                break
            else:
                if not money_machine.make_payment(choice_check.cost):
                    break
                else:
                    coffee_maker.make_coffee(choice_check)