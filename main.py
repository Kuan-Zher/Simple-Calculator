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

#Addition/ Subtraction/ Division/ Multiplication
def simple_arithmetic():

    #Prompt for user input
    num1 = "Enter first number: "
    num2 = "Enter second number: "

    #Perform Operations
    operator = input("Choose an operator (+, -, //, * or 'exit' back to main menu)")
    if operator == "+":
        num1 = float(input(num1))
        num2 = float(input(num2))
        print("Addition: {} + {} = {}".format(num1,num2,num1+num2))
    elif operator == "-":
        num1 = float(input(num1))
        num2 = float(input(num2))
        print("Subtraction: {} - {} = {}".format(num1,num2,num1-num2))
    elif operator == "//":
        num1 = float(input(num1))
        num2 = float(input(num2))
        print("Division: {} // {} = {}".format(num1,num2,num1//num2))
    elif operator == "*":
        num1 = float(input(num1))
        num2 = float(input(num2))
        print("Multiplication: {} * {} = {}".format(num1,num2,num1*num2))
    elif operator == "exit":
        print("Exiting...")
        return
    else:
        print("Invalid input. Please try again.\n")
        simple_arithmetic()


    return

def trigonometry():
    return

def exponents():
    return

def square_root():
    return

def percentage():
    return

show_menu()