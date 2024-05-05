"""
Author: S.Sunhaloo
Date: 05/05/2025

Simple Palidrome Check what will also create a file which
will add all the data ( user_input ) / user inputs into a file called 'input.txt'
If that file does not exists; then create it. If does does exists, meaning an Exception will be raised
"FileExistsError"; if that is raised continue to append to file
Made with Neovim using Ruff-LSP
"""


# create function to add user's value into text file
def open_file_append(user_input):
    # context manager
    try:
        with open("input.txt", "x") as file:
            # adds the value to `input.txt`
            file.write(f"\n{user_input}")
    except FileExistsError:
        with open("input.txt", "a") as file:
            # adds the value to `input.txt`
            file.write(f"\n{user_input}")


# create function to read that file
def open_file_read():
    # context manager
    with open("input.txt", "r") as file:
        # reads each line in file
        for line in file:
            print(line)


# main function
def main():
    # ask the user to input the value
    user_input = input("Please Enter Number to Check if Palindrome: ")

    # call the function to add user's value to file
    open_file_append(user_input)

    # check if palidrome
    if user_input == user_input[::-1]:
        # if palidrome
        print("\nValue is a Palidrome!\n")
    else:
        # if NOT palidrome
        print("\nValue is Not a Palidrome\n")


# calling main function together with the function that will open file for read
print()
main()
print("-" * 40)
print("\nData Users Entered:")
open_file_read()
