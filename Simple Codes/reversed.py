# Calculator Program

# Global Variables
global num1
global num2

# Defining Global Variables
# Else they will not work below ( in the "insert_values" function )
num1 = 0
num2 = 0

# Function "display" will display the "choices"
def display():

    print()
    print("Calculator Program")
    print()

    print("USAGE: Type Down The Number To Use Mathematical Operations On Numbers")

    print()
    print("Addition --> 1")
    print()
    
    print("Subtraction --> 2")
    print()

    print("Multiplication --> 3")
    print()

    print("Division --> 4")
    print()

# Function with identifier name "insert_values"
def insert_values():

    # Exception Handling
    try:

    # Using Global Function to change the values of "num1" and "num2"
        global num1
        global num2

    # Asking the user to enter values
        num1 = float(input("Enter Value For Number 1: "))
        num2 = float(input("Enter Value For Number 2: "))

    # If user enters any other data type other than "real number"
    except ValueError:

        # Output appropriate message
        print()
        print("Please Enter Real Numbers Only!")
        print()

# Function with identifier name "add" will add the numbers
def add(x, y):

    # Performing Addition
    total = x + y
    positive_value = abs(x + y)

    # Displaying the results
    print()
    print(f"Real Answer = {total}")
    print()
    print(f"Positive Answer = {positive_value}")

# Function with identifier name "sub" will subtract the number
def sub(x, y):

    # Performing Subtraction
    answer = x - y
    negative_value = y - x

    # Displaying the results
    print()
    print(f"Real Answer = {answer}")
    print()
    print(f"Negative Answer = {negative_value}")

# Function with identifier name "multiply" will perform multiplication on the numbers
def multiply(x, y):

    # Performing Multiplication
    positive_value = abs(x * y)
    negative_value = x * y

# Displaying the results
    print()
    print(f"Real Answer = {positive_value}")
    print()
    print(f"Negative Answer = {negative_value}")

# Function with identifier name "division" will perform divison on the numbers
def division(x, y):

    # Performing Division
    answer = x / y
    round_answer = x // y
    inverse_answer = y / x
    inverse_round_answer = y // x

# Displaying the results
    print()
    print(f"Real Answer = {answer}")
    print()
    print(f"Round Off Answer = {round_answer}")
    print()
    print(f"Inverse Answer = {inverse_answer}")
    print()
    print(f"Inverse Round Off Answer = {inverse_round_answer}")

# Function "main_calc" will prompt the user to enter his/her choices
def main_calc():

# Exception Handling
    try:

        # Variable "user_choice" will ask the user to enter his choices
        user_choice = int(input("Please Enter Your Choice: "))

        # CASE OF OTHERWISE ENDCASE
        match user_choice:

            # Addition
            case 1:

                # Calling Function inside the "main_calc" function
                insert_values()
                print()
                print("Addition Results")
                add(num1, num2)

            # Subtraction
            case 2:

                # Calling Function inside the "main_calc" function
                insert_values()
                print()
                print("Subtraction Results")
                sub(num1, num2)

            # Multiplication
            case 3:

                # Calling Function inside the "main_calc" function
                insert_values()
                print()
                print("Multiplication Results")
                multiply(num1, num2)

            # Division
            case 4:

                # Calling Function inside the "main_calc" function
                insert_values()
                print()
                print("Division Results")
                division(num1, num2)

            # If user does not type the correct number
            case _:

                print()
                print("Something Went Wrong!")
                print()

    # If user enter any other data type other than "integer" values
    except ValueError:

        # Output the appropriate message
        print()
        print("Please Enter Integer Numbers Only!")
        print()
        
# Calling Functions
display()
main_calc()

# The user need to close the file
while True:
    pass

# S.Sunhaloo
