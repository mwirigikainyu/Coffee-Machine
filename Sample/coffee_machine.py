from money import Money
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18, },
        "cost": 10.50,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24, },
        "cost": 20.50,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24, },
        "cost": 30.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_running = True
while machine_running:
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'report':
        print(resources)
    elif order in MENU.keys():
        cost = MENU[order]['cost']
        ingredients = MENU[order]['ingredients']
        for resource in resources:
            if ingredients[resource] <= resources[resource]:
                # check resources and deduct resources used
                resource_value = resources[resource] - ingredients[resource]
                # update resources in stock
                resources[resource] = resource_value
                # ask for payment if resources are available
                payment = float(input(f'The total cost is ${MENU[order]["cost"]} \nPlease insert cash:'))
                # check if payment is enough
                if payment >= cost:
                    change = payment - cost
                    # serve order and give change
                    print(f"Here is your ☕️. {order.title()}. Enjoy!")
                    print(f"Your change is {Money(amount=change, currency='KSH')}")
                    break
                else:
                    print(f"Sorry, {Money(amount=payment, currency='KSH')} is not enough for the drink")
            else:
                print(f'Sorry! We do not have enough {resource}.')
                print("""
                                                                                                                
 ,-----.           ,--.              ,---.     ,---.                          ,--.              
'  .-.  ',--.,--.,-'  '-.     ,---. /  .-'    '   .-'  ,---. ,--.--.,--.  ,--.`--' ,---. ,---.  
|  | |  ||  ||  |'-.  .-'    | .-. ||  `-,    `.  `-. | .-. :|  .--' \  `'  / ,--.| .--'| .-. : 
'  '-'  ''  ''  '  |  |      ' '-' '|  .-'    .-'    |\   --.|  |     \    /  |  |\ `--.\   --. 
 `-----'  `----'   `--'       `---' `--'      `-----'  `----'`--'      `--'   `--' `---' `----' 
                                                                                                
                """)
                machine_running = False
                break
    else:
        print('That order is not in our menu')
