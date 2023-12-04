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
    operator = input("Choose an operator (+, -, //, *)")
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
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    
    result = base ** exponent
    print(f"Result: {base}^{exponent} = {result}")
    return

#Return the square root of the number entered
def square_root():

    num = input("Enter the number to square root (Enter 'stop' to exit to main menu): ")

    #Check if user wants to exit to main menu
    if (num.lower() == "stop"):
        return
    
    print("---------------------------------------------------------------------")

    #Catch any invalid inputs and calculate square root
    try:
        root = float(math.sqrt(float(num)))
        print("The square root of {} is: {:.3f}\n".format(num,root))
    except (ValueError):
        print("That is not a valid number. Try again.\n")
        square_root()

    return

def percentage():
    return

show_menu()