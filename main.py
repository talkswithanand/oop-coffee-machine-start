from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# objects below for all access to classes
resources = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

repeat_statement = True
while repeat_statement:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        repeat_statement = False
    elif choice == "report":
        resources.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if resources.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            resources.make_coffee(drink)



