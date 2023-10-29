# Program Code

# import os module
import os

# path of file
path = "/data/data/com.termux/files/home/storage/shared/Programming/Python/Data.txt"

# array with identifier name "Data"
Data = []

# function checking will allow us to check if file
    # exists
    # is a file
    # or is a directory
def checking(location):

    # check if file exists
    # exception handling
    try:

        print()
        print(f"Does File Exists: {os.path.exists(location)}")
        print()

        print(f"Is File An Actual File: {os.path.isfile(location)}")
        print()
        print(f"Is It A Direcory: {os.path.isdir(location)}")
        print()

    # if file is not found
    except FileNotFoundError:

        print()
        print("File Has Not Been Found")
        print()


# reading file
def readfile(location):

    # opening file
    FileOpenRead = open(path, "r")

    # reading each line in file
    for line in FileOpenRead:

        # appends data from "Data.txt" into "Data" array
        Data.append(int(line))

    # closing file
    FileOpenRead.close()

    # check if file is closed
    print()
    print(f"Is File Closed: {FileOpenRead.closed}")
    print()

# displaying array
def display(array):

    # if array is empty
    if not array:

        print()
        print("Array is empty")
        print()
    
    # if array is not empty
    else:

        for x in array:

            print(f"{x} ", end="")

        print()

# binary search
def b_search(array, item):

    return b_calc(0, len(array) -1, array, item)

def b_calc(lower, upper, array, item):

    counter = 0
    
    while lower <= upper:

        mid = (lower + upper) // 2

        if array[mid] == item:

           counter += 1

        elif mid < item:

            # removes the lower part of array
            lower = mid + 1

        else:

            # removes the upper part of array
            upper = mid - 1

    print(f"Number Appeared {counter}")

    return -1

# ask the user for number
    # counts the number of time number appears
def user_number(array, item):

    # exception handling
    try:

        user_input = int(input("Please Enter A Number: "))
        
        if user_input >= 0 and user_input <= 100:

            # calls binary search
            b_search(array, item)

        else:

            print()
            print("Your Input Is Not In Range")
            print()

    except ValueError:

        print()
        print("Please Enter Integer Values Only!")
        print()

# calling function
display(Data)

checking(path)

readfile(path)

display(Data)

user_number(Data, 5)
