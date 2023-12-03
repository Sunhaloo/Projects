# Factorial Solver

# Recursive Function

    # This is my first Recursive Function ever!
    # I will be explaining myself how it works in this Python file using comments

# So Recursive Function is one that calls itself ( in a way )

# So there are 2 things to know:
    # 1. Base Statement(s)
    # 2. Recursive Procedure / Statement(s)

# We need to write ( understand ) the 2. Recursive Procedure / Statement(s) part
# Then after that; we write the 1. Base Statement(s)

# Explanations on Factorial Function

# What's the Factorial of a number?
# For example: The factorial of 3 will be:
    # 3! = 3 * 2 * 1
# or for 4 we have:
    # 4! = 4 * 3 * 2 * 1

# Hence we could have a function called "fact" that take an argument
# Therefore we could do:

    # fact(3) = 3 * 2 * 1
    # fact(4) = 4 * 3 * 2 * 1

# But we can also write fact(4) as:

    # fact(4) = 4 * fact(3) ---> The Recursive Part!

# Bascially the same thing

# Thus, we can get a formula:

    # fact(num) = num * fact(num -1)

# Lets get to coding

# Function frac() will perform the calculations
def fact(num):

    # Base Statement
    if num == 1:

        return 1

    # Recursive Procedure
    else:

        # Apply Formula
        return num * fact(num -1)

# Making the program
print()
print("Factorial Calculator")
print()

# Let user enter the number to find the Factorial for:
try:

    user_number = int(input("Please Enter A Number: "))

except ValueError:

    print()
    print("Please Enter Integer Numbers Only!")
    print()


# Passing the user's number into the Factorial Function and placing it in a variable
result = fact(user_number)

# Displaying Answer
print()
print(f"The Result of {user_number} = {result}")
print()
