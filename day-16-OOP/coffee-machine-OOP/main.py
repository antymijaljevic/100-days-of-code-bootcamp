from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_working = True

""" main """
while machine_working:
    consumer_input = input(f"\nWhat would you like? ({menu.get_items()}): ").lower()

    """ consumer choose """
    if consumer_input == "off":
        machine_working = False
    elif consumer_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(consumer_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)