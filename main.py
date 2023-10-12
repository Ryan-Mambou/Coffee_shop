resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

# variable to monitor the continuation of the game
coffee_monitor = True


def using_resources(original_resources, coffee_name):
    for resource in original_resources:
        if coffee_name == 'latte':
            if resource == 'Water':
                original_resources[resource] -= 200
            elif resource == 'Milk':
                original_resources[resource] -= 10
            elif resource == 'Coffee':
                original_resources[resource] -= 15
        elif coffee_name == 'espresso':
            if resource == 'Water':
                original_resources[resource] -= 100
            elif resource == 'Milk':
                original_resources[resource] -= 20
            elif resource == 'Coffee':
                original_resources[resource] -= 10
        elif coffee_name == 'cappuccino':
            if resource == 'Water':
                original_resources[resource] -= 150
            elif resource == 'Milk':
                original_resources[resource] -= 15
            elif resource == 'Coffee':
                original_resources[resource] -= 20


def update_resources_money(original_resource, coffee_name):
    if coffee_name == "espresso":
        original_resource['Money'] += 2.5
    elif coffee_name == "latte":
        original_resource['Money'] += 2.0
    elif coffee_name == "cappuccino":
        original_resource['Money'] += 3.0


def calculate_money(quarter, dime, nickle, pennie):
    total = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (pennie * 0.01)
    return round(total, 2)


def calculate_balance(amount_paid, coffee_name):
    if coffee_name == 'espresso':
        return round(amount_paid - 2.5, 2)
    elif coffee_name == 'latte':
        return round(amount_paid - 2.0, 2)
    else:
        return round(amount_paid - 3.0, 2)


def checking_money(coffee_name, amount):
    """function which return True if amount is enough and False if not"""
    return coffee_name == 'espresso' and amount > 2.5 or coffee_name == 'latte' and amount > 2.0 or coffee_name == 'cappuccino' and amount > 3.0


def checking_resources(original_resources, coffee_name):
    for resource in original_resources:
        if coffee_name == 'espresso':
            if resource == 'Water':
                if original_resources[resource] - 200 < 0:
                    return "Not enough Water"
            elif resource == 'Milk':
                if original_resources[resource] - 10 < 0:
                    return "Not enough Milk"
            elif resource == "Coffee":
                if original_resources[resource] - 15 < 0:
                    return "Not enough Coffee"
        elif coffee_name == 'latte':
            if resource == 'Water':
                if original_resources[resource] - 100 < 0:
                    return "Not enough Water"
            elif resource == 'Milk':
                if original_resources[resource] - 20 < 0:
                    return "Not enough Milk"
            elif resource == "Coffee":
                if original_resources[resource] - 10 < 0:
                    return "Not enough Coffee"
        elif coffee_name == 'cappuccino':
            if resource == 'Water':
                if original_resources[resource] - 150 < 0:
                    return "Not enough Water"
            elif resource == 'Milk':
                if original_resources[resource] - 15 < 0:
                    return "Not enough Milk"
            elif resource == "Coffee":
                if original_resources[resource] - 20 < 0:
                    return "Not enough Coffee"
        else:
            return "Please insert the coffee name correctly"
    return ""


def toggle_coffee_monitor():
    return not coffee_monitor


def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino)? ")
    if choice == 'report':
        for resource in resources:
            resources[resource] = str(resources[resource] + 100) + "ml"
    elif choice == 'off':
        toggle_coffee_monitor()
    else:
        resource_check = checking_resources(resources, choice)
        if resource_check == "":
            using_resources(resources, choice)
            print(resources)
            print("Insert coins:")
            pennies = int(input("How many pennies: "))
            nickles = int(input("How many nickles: "))
            dimes = int(input("How many dimes: "))
            quarters = int(input("How many quarters: "))

            total_paid = calculate_money(quarters, dimes, nickles, pennies)

            money_check = checking_money(choice, total_paid)

            if not money_check:
                print("Sorry, that's not enough money. Money refunded")
            else:
                update_resources_money(resources, choice)
                balance = calculate_balance(total_paid, choice)
                if balance > 0:
                    print(f"Here is your balance: {balance}")
                print(f"Here is your {choice}. Enjoy!")
        else:
            print(resource_check)
            coffee_machine()


while coffee_monitor:
    coffee_machine()
