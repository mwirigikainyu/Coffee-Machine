from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
accounts = MoneyMachine()
# ------------------------------------------------------------------
machine_is_on = True
while machine_is_on:
    # get order
    order = input(f"Welcome to Joe's Coffee. Our Menu today includes: "
                  f"\n{menu.get_items()}"
                  f"\nWhat would you like to order?").lower()
    if order == 'report':
        coffee_maker.report()
        accounts.report()
    elif order == 'off':
        machine_is_on = False
    else:
        # find order in menu
        if menu.find_drink(order):
            menu_item = menu.find_drink(order)
            # check if resources are sufficient
            if coffee_maker.is_resource_sufficient(menu_item):
                # process payment
                if accounts.make_payment(menu_item.cost):
                    # make coffee and serve
                    coffee_maker.make_coffee(menu_item)
            else:
                break
