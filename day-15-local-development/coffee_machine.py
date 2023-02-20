from data import *
from os import name, system


def clear_terminal():
    """ 
        clears screen depends on a OS type
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')
        
        
def show_report():
    """
        returns a report with resources and balance
    """
    print("\n")
    for key, value in resources.items():
        if key == "water" or key == "milk":
            print(f"{key.capitalize()}: {value}ml")
        elif key == "coffee":
            print(f"{key.capitalize()}: {value}g")
        else:
            print(f"{key.capitalize()}: ${value}")


def check_resources(coffe_ing):
    """
        receives coffee ingredients and returns 
        boolean value depends on resource availability  
    """
    for key, value in coffe_ing.items():
        if key == "water" and not value <= resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif key == "coffee" and not value <= resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
        elif key == "milk" and not value <= resources["milk"]:
            print("Sorry there is not enough milk.")
            return False
            
    return True

def deduct_resources(coffee_res):
    """
        takes away coffee resources and the money
    """
    global resources
    
    resources["money"] += coffee_res["cost"]
    
    for key, value in coffee_res["ingredients"].items():
        if key == "water":
            resources[key] -= value
        elif key == "coffee":
            resources[key] -= value
        elif key == "milk":
            resources[key] -= value
            
    return True


def check_money(quarters, dimes, nickel, penny, money_needed):
    """
        receives types of coins sum them up and returns change
    """
    global resources
    
    quarters_total = quarters * coin_types["quarters"]
    dimes_total = dimes * coin_types["dimes"]
    nickel_total = nickel * coin_types["nickel"]
    penny_total = penny * coin_types["penny"]
    values = [quarters_total, dimes_total, nickel_total, penny_total]
    
    if sum(values) >= money_needed:
        change = sum(values) - money_needed
        if change > 0:
            return change
        else:
            return True
    else:
        print("\nSorry that's not enough money. Money refunded.")
        resources["money"] -= money_needed
        return False
    
def main():
    """
        main function
    """
    
    """ clear terminal """
    clear_terminal()
    
    while True:
        """ ask buyer """
        buyer_input = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        
        """ print report if asked """
        if buyer_input == "report":
            show_report()
            continue
        
        """ check resources """
        if not check_resources(MENU[buyer_input]['ingredients']):
            continue
        
        """ deduct resources """
        deduct_resources(MENU[buyer_input])
        
        """ ask for coins """
        print("\nPlease insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickel = int(input("How many nickel?: "))
        penny = int(input("How many penny?: "))
        
        """ if enough money """
        change = check_money(quarters=quarters, dimes=dimes, nickel=nickel, penny=penny, money_needed=MENU[buyer_input]['cost'])
        if not change:
            continue
        
        """ give the drink to a customer """
        print("\n")
        if type(change) == float:
            print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {buyer_input}. Enjoy!")

if __name__ == '__main__':
    main()