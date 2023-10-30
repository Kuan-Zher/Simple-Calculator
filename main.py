import math

def show_menu():
    print("+-------------------+")
    print("| Simple Calculator |")
    print("+-------------------+")
    print("\nWhat do you want to do?")
    print("------------------------")
    print("1 | Standard Arithmetic")
    print("2 | Trigonometry")
    print("3 | Exponents")
    print("4 | Square Root")
    print("5 | Percentage")

    response = int(input("Enter your option: "))
    
    if response == 1:
        simple_arithmetic()
    elif response == 2: 
        trigonometry()
    elif response == 3: 
        exponents()
    elif response == 4:
        square_root()
    elif response == 5:
        percentage()
    else:
        print("Unrecognized response")
    
    show_menu()

def simple_arithmetic():
    return

def trigonometry():
    return

def exponents():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    
    result = base ** exponent
    print(f"Result: {base}^{exponent} = {result}")
    return

def square_root():
    return

def percentage():
    return

show_menu()