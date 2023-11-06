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
    print("Select a trigonometric function to perform")
    print("------------------------------------------")
    print("1 | Sin")
    print("2 | Cos")
    print("3 | Tan")
    print("4 | Inverse Sin")
    print("5 | Inverse Cos")
    print("6 | Inverse Tan")
    trigonometric_function = int(input("Selected trigonometric function: "))
    number = float(input("x: "))

    if trigonometric_function == 1:
        print(f"sin(x) is {math.sin(number)}")
    elif trigonometric_function == 2: 
        print(f"cos(x) is {math.cos(number)}")
    elif trigonometric_function == 3: 
        print(f"tan(x) is {math.tan(number)}")
    elif trigonometric_function == 4:
        print(f"tan(x) is {math.asin(number)}")
    elif trigonometric_function == 5:
        print(f"tan(x) is {math.acos(number)}")
    elif trigonometric_function == 6:
        print(f"tan(x) is {math.atan(number)}")
    else:
        print("Unrecognized response")
        

def exponents():
    return

def square_root():
    return

def percentage():
    return

show_menu()