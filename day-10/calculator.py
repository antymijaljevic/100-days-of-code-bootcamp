from art import logo

def add(num1, num2):
    """
        add two numbers
    """
    return num1 + num2

def subtract(num1, num2):
    """
        subtract two numbers
    """
    return num1 - num2

def multiply(num1, num2):
    """
        multiply two numbers
    """
    return num1 * num2

def divide(num1, num2):
    """
        divide two numbers
    """
    return num1 / num2


""" possible operations """ 
operations = {
        "+": add, 
        "-": subtract, 
        "*": multiply, 
        "/": divide
    }

def calculator():
    """ 
        main function &
        user input num 1
    """ 
    print(logo)
    num1 = float(input("What's the first number?: "))

    """ show user possible operations """
    for sym in operations:
        print(sym)
        
    while True:
        """ user input num2 """
        operation_sym = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        """ show user result """
        operation = operations[operation_sym]
        answer = operation(num1, num2)
        print(f"{num1} {operation_sym} {num2} = {answer}")
        
        """ continue or exit """
        con_or_exit = input(f"\nType 'y' to continue calculating with {answer} or type 'n' to start new calculation: ").lower()
        if con_or_exit == 'y':
            num1 = answer
            continue
        elif con_or_exit == 'n':
            calculator()
        else:
            break

""" main """
calculator()