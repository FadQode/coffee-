menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "americano": {
        "ingredients": {
           "water": 50,
           "coffee": 20
        },
        "cost": 1.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 3 Report method
def resource_report(resources):
    """Format resource into printable format: water, milk and coffee"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f" water: {water}ml \n milk: {milk}ml \n coffee: {coffee}ml \n money: ${money} "

# TODO 4 check resource sufficient
def check(user_choice, resources, menu):
    """check if the resources is enough"""
    if resources ["water"] < menu[user_choice]["ingredients"]["water"]:
        return False
    elif resources ["coffee"] < menu[user_choice]["ingredients"]["coffee"]:
        return False
    elif not "milk" in menu[user_choice]["ingredients"]:
        return True
    elif resources ["milk"] < menu[user_choice]["ingredients"]["milk"]:
        return False
    else:
        return True



# TODO 5 Process Coin
def coin(user_money):
    """process coin the user has into $$$"""
    quarter = float(input("put quarter: "))
    dimes = float(input("put dimes: "))
    nickles = float(input("put nickles: "))
    pennies = float(input("put pennies: "))
    user_money = (quarter * 0.25) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return user_money



# TODO 7 make coffee and decrease resource everytime coffe was make
def success(user_choice, resources, menu):
    """ decrease resource everytime a coffee was made"""
    resources["water"] -= menu[user_choice]["ingredients"]["water"]
    resources["coffee"] -= menu[user_choice]["ingredients"]["coffee"]
    if not "milk" in menu[user_choice]["ingredients"]:
        return
    resources["milk"] -= menu[user_choice]["ingredients"]["milk"]
    return

# TODO 8 make coffee machine a function
def coffee_machine(resources, menu):
    # TODO 2 turn off method
    switch = True
    money =  0
    while switch:
        user_choice = input("choose your coffee. latte/espresso/cappucino \n press the report button to see resources: ")
        resources["money"] = money
        if user_choice == "report" :
            print(resource_report(resources))
        elif user_choice in menu:
            if check(user_choice, resources, menu):
                user_money = 0
                user_money = coin(user_money)
                # TODO 6 Check transaction successful
                if user_money >= menu[user_choice]["cost"]:
                    money += menu[user_choice]["cost"]
                    success(user_choice, resources, menu)
                    print(f"here is your {user_choice} enjoy!")
                    if user_money > menu[user_choice]["cost"]:
                        exchange = user_money - menu[user_choice]["cost"]
                        print(f"and here is ${round(exchange, 2)} ")
                else:
                    print("sorry that's not enough money. Money refunded.")
            else:
                print("sorry not enough resources")
        else:
            switch = False

coffee_machine(resources, menu)










# See PyCharm help at https://www.jetbrains.com/help/pycharm/
