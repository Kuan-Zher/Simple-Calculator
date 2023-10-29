import math

def show_menu():
    print("\n+-------------------+")
    print("| Simple Calculator |")
    print("+-------------------+")
    print("\nWhat do you want to do?")
    print("------------------------")
    print("1 | Standard Arithmetic")
    print("2 | Trigonometry")
    print("3 | Exponents")
    print("4 | Square Root")
    print("5 | Percentage")

    response = int(input("\nEnter your option: "))
    
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
        print("\nUnrecognized response")
    
    show_menu()

def simple_arithmetic():
    return

def trigonometry():
    return

def exponents():
    return

def square_root():
    return

def percentage():
    # Error handling 1: Cannot divide any number by 0 (denominator)

    neumerator = float(input("\nEnter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    percentage = (neumerator/denominator)*100

    print(f"The percentage of {neumerator}/{denominator} is {percentage:.5}%")
    return 

show_menu()