from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    answer = input(f"What would you like? {options}: ")

    if answer == "off":
        is_on = False

    elif answer == "report":
        coffee_maker.report()
        my_money_machine.report()

    else:
        drink = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


