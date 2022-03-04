from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
is_cont = True

while is_cont:
    user_input = input(f"What would you like to have today? Here is our menu {coffee_menu.get_items()}:  ").lower()
    if user_input == "off":
        is_cont = False
    elif user_input == "report":
        coffee_maker.report()
        money.report()
    else:
        item = coffee_menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(item):
            if money.make_payment(item.cost):
                coffee_maker.make_coffee(item)
        else:
            is_cont = False



