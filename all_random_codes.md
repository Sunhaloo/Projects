---
Alias: Random Python Program Codes
Tag: python
Author: S.Sunhaloo
Type: Random Program Code
Date: 2023-09-09
Status: HOLD
---

## List of Contents

- [[Random HSC Python Codes#Code 1| Code 1]]
- [[Random HSC Python Codes#Code 2 | Code 2]]
- [[Random HSC Python Codes#Code 3 | Code 3]]
- [[Random HSC Python Codes#Code 4 | Code 4]]
- [[Random HSC Python Codes#Code 5 | Code 5]]
- [[Random HSC Python Codes#Code 6 | Code 6]]
- [[Random HSC Python Codes#Code 7 | Code 7]]
- [[Random HSC Python Codes#Code 8 | Code 8]]
	- [[Random HSC Python Codes#Code 8 ( my shitty version ) | Code 8 My Version]]
- [[Random HSC Python Codes#Code 9 | Code 9]]
- [[Random HSC Python Codes#Code 9 | Code 9]]

---

My Links

- [[Random HSC Python Codes#Socials | Link to Socials]]

---

# Code 1:

This code was given by Miss Nafeeza Coan. This program was originally in [[Visual Basic Language]] and we ( [[Python Language | python]] ) had to convert the code, because the majority of people Visual Basic over Python was large

Date Given: 7th September 2023
Date Completed: 10th September 2023

```python

# Random Program Code 1

print()

# DECLARE anime: ARRAY[0:5] OF STRING
anime = ["EREN", "LEVI", "GOJO", "TANJIRO", "NEZUKO", "MAI"]

# DECLARE subject: ARRAY[0:5] OF STRING
subject = ["COMPUTER", "SOCIOLOGY", "ARABIC", "ENGLISH", "FRENCH", "JAPANESE"]

# DECLARE arrayStack: ARRAY[0:4] OF STRING
arrayStack = ["ROSE", "BOGAINLAVILLAIN", "LILY", "LAVENDER", "JASMINE"]

# DECLARE fruits: ARRAY[0:5] OF STRING
fruits = ["Grape", "Kiwi", "Apple", "Mango", "Banana", "Orange"]

# DECLARE num: ARRAY[0:4] OF INTEGER
num = [12, 45, 23, 45, 55]

# Functions and Procedures
# Functions To Display Arrays
# Function with identifier name "display_anime" which will display array "anime"
def display_anime():

    # If array is empty
    if not anime:

        print()
        print("Array Is Empty!")
        print()

    else:

        for x in anime:  

            # Outputs the value of array on separate lines
            print(x)

# Function with identifier name "display_subject" to display the array "subject"
def display_subject():

    # If array is empty
    if not subject:

        print()
        print("Array Is Empty!")
        print()

    else:

        for x in subject:  

            # Outputs the value of array on separate lines
            print(x)

# Function with identifier name "display_num" to display array "num"
def display_num():

    # If array is empty
    if not num:

        print()
        print("Array Is Empty!")
        print()

    else:

        for x in num:

            # Outputs the value of array on separate lines
            print(x)

# Function with identifier name "Inseriton_Sort_Number" which will sort our array "num"
# Function "Insertion_Sort_Number" will perform the calculation
def Insertion_Sort_Number(num):

    # Variable array_length will store the length of the array
    array_length = len(num)

    # Insertion Sort compares second values with previous value
    for i in range(1, array_length):

        # Storing the values stored at "i"
        value_i = num[i]

        # Storing the "previous" address of "i"
        j = i - 1

        # Condition to enter loop
        while j >= 0 and num[j] > value_i:

            # Swapping Part of Algorithm
            num[j + 1] = num[j]

            # Counter / Address of "j" decreases by 1
            j -= 1

        # If array is already sorted, "returns array"
        num[j + 1] = value_i

# Function with identifier name "Insertion_Sort_String" which will sort our array "anime"
# Function "Insertion_Sort_String" will perform the calculation
def Insertion_Sort_String(anime):

    # Variable array_length will store the length of the array
    array_length = len(anime)

    # Insertion Sort compares second values with previous value
    for i in range(1, array_length):

        # Storing the values stored at "i"
        value_i = anime[i]

        # Storing the "previous" address of "i"
        j = i - 1

        # Condition to enter loop
        while j >= 0 and anime[j] > value_i:

            # Swapping Part of Algorithm
            anime[j + 1] = anime[j]

            # Counter / Address of "j" decreases by 1
            j -= 1

        # If array is already sorted, "returns array"
        anime[j + 1] = value_i

# Insertion Sort Page ( Sub Page )
# Function with identifier name "InsertionSort" will be our sub page ( for insertion sort )
def InsertionSort():

    # Insertion Sort Main Page ( Overall it's a sub page )
    print()
    print("Insertion Sort Sub Page")
    print()
    print("----------")
    print()
    print("Insertion Sort Integers: 1")
    print()
    print("Insertion Sort Strings: 2")
    print()
    print("Exit Program: 3")
    print()

    # Ask the user to enter his choice for insertion sort sub-page
    # Exception Handling
    try:

        # Ask the user to enter a choice for insertion sort sub-page
        choice_insertion_sort = int(input("Please Enter A Choice From The Above Choices: "))

    # If users anything character except of integers
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

    # Provides Corresponding Respond To User Choice
    if choice_insertion_sort == 1:

        print()
        print("Array Before Insertion Sort:")
        print()

        # Calling function "display_num" to display the contents of array "num"
        # This is to show the user what the array looked like BEFORE applying Insertion Sort
        display_num()

        print()
        print("Array After Insertion Sort:")

        # Calling the function "Insertion_Sort_Number" to arrange the numbers in ascending order
        Insertion_Sort_Number(num)

        print()

        # Displaying the array again
        # This is show the user what the array looks AFTER applying Insertion Sort

        display_num()

        print()

    elif choice_insertion_sort == 2:

        print()
        print("Array Before Insertion Sort:")
        print()

        # Calling function "display_anime" to display the contents of array "anime"
        # This is to show the user what the array looked like BEFORE applying Insertion Sort

        display_anime()

        print()
        print("Array After Insertion Sort:")

        # Calling the function "Insertion_Sort_Number" to arrange the numbers in ascending order
        Insertion_Sort_String(anime)

        print()

        # Displaying the array again
        # This is show the user what the array looks AFTER applying Insertion Sort

        display_anime()
        print()

# Function with identifier name "BubbleSort_Number" which will sort our array "num"
# Function "BubbleSort_Number" will perfom the calculation
def BubbleSort_Number(num):

    # Calculating the length of array "num"
    length_array = len(num)

    # Variable "update" will "tell" up if the value has been swapped
    update = True

    # Variable "swap" will keep track of how many times valus has been swapped
    swap = 0

    # Condition to enter "while" loop
    while update == True and length_array > 0:

        # "update" need to become "False" to be "updated"
        update = False

        # Number of times it will sort the array
        for x in range(0, length_array - 1):

            # Checks ever value in the array
            for y in range(0, length_array - 1):

                # Sorting the array in Ascending Order
                if num[y] > num[y +1]:

                    # Sorting Part of Algorithm
                    temp = num[y]
                    num[y] = num[y + 1]
                    num[y + 1] = temp

                    # "update" become "True"
                    update = True

                    # "swap" increases by 1
                    swap += 1

# Function with identifier name "BubbleSort_Anime" which will sort our array "num"
# Function "BubbleSort_Anime" will perfom the calculation
def BubbleSort_Anime(anime):

    # Calculating the length of array "anime"
    length_array = len(anime)

    # Variable "update" will "tell" up if the value has been swapped
    update = True

    # Variable "swap" will keep track of how many times valus has been swapped
    swap = 0

    # Condition to enter "while" loop
    while update == True and length_array > 0:

        # "update" need to become "False" to be "updated"
        update = False

        # number of times it will sort the array
        for x in range(0, length_array - 1):

            # Checks ever value in the array
            for y in range(0, length_array - 1):

                # Sorting the array in Ascending Order
                if anime[y] > anime[y +1]:

                    # Sorting Part of Algorithm
                    temp = anime[y]
                    anime[y] = anime[y + 1]
                    anime[y + 1] = temp

                    # "update" become "True"
                    update = True

                    # "swap" increases by 1
                    swap += 1

# Bubble Sort ( Sub-Page )
# Function with identifier name "BubbleSort" will be our sub page ( for bubble sort )
def BubbleSort():

    # Bubble Sort Main Page ( Overall sub page )
    print()
    print("Bubble Sort Sub Page")
    print()
    print("----------")
    print()
    print("Bubble Sort Integers: 1")
    print()
    print("Bubble Sort Strings: 2")
    print()
    print("Exit Program: 3")
    print()

    # Ask the user to enter his choice for bubble sort sub-page
    # Exception Handling
    try:

        # Ask the user to enter a choice for bubble sort sub-page
        choice_bubble_sort = int(input("Please Enter A Choice From The Above Choices: "))

    # If users anything character except of integers
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

    # Provides Corresponding Respond To User Choice
    if choice_bubble_sort == 1:

        print()
        print("Array Before Bubble Sort:")
        print()

        # Calling function "display_num" to display the contents of array "num"
        # This is to show the user what the array looked like BEFORE applying Bubble Sort
        display_num()

        print()
        print("Array After Bubble Sort:")

        # Calling the function "Bubble_Sort_Number" to arrange the numbers in ascending order

        BubbleSort_Number(num)

        print()

        # Displaying the array again
        # This is show the user what the array looks AFTER applying Bubble Sort

        display_num()

        print()

    elif choice_bubble_sort == 2:

        print()
        print("Array Before Insertion Sort:")
        print()

        # Calling function "display_anime" to display the contents of array "anime"
        # This is to show the user what the array looked like BEFORE applying Insertion Sort

        display_anime()

        print()
        print("Array After Insertion Sort:")

        # Calling the function "BubbleSort_Anime" to arrange the numbers in ascending order
        BubbleSort_Anime(anime)

        print()

        # Displaying the array again
        # This is show the user what the array looks AFTER applying Insertion Sort

        display_anime()

        print()

    else:

        # Exits program entirely
        print()
        print("Exiting Program")
        print()

        exit

# Function with identifier name "LinearSearch_Number" which will search for a value in array "num"
# Function "LinearSearch_Number" will perfom the calculation

def LinearSearch_Number(num):

    # A variable that will be used to use in for LinearSearch_Number
    # Exception Handling

    try:

        # Ask the user to enter a value to search
        Linear_Input_Number = int(input("Please Enter A Value To Search: "))

    except ValueError:

        print()
        print("Please Enter Integer Values!")
        print()    

    # Calculating the length of array "num"
    length_array = len(num)

    # Stepping through the num
    for i in range(0, length_array):

        # If "value" is found
        if num[i] == Linear_Input_Number:

            # It returns the Address of the array
            return i

    # If "Linear_Input_Num" has not been found
    # "return - 1" == Error / Not Found
    return - 1

# Function with identifier name "LinearSearch_String" which will search for a value in array "anime"
# Function "LinearSearch_String" will perfom the calculation
def LinearSearch_String(anime):

    # A variable that will be used to use in for LinearSearch_String
    # Exception Handling
    try:

        # Ask the user to enter a value to search
        Linear_Input_String = str(input("Please Enter A Value To Search: "))

    except ValueError:

        print()
        print("Please Enter Integer Values!")
        print()

    # Calculating the length of array "anime"
    length_array = len(anime)

    # Stepping through the array "anime"
    for i in range(0, length_array):

        # If "value" is found
        if anime[i] == Linear_Input_String:

            # It returns the Address of the array
            return i

    # If "Linear_Input_String" has not been found
    # "return - 1" == Error / Not Found
    return - 1

# Linear Search ( Sub-Page )
# Function with identifier name "LinearSearch" will be our sub page ( for linear search )
def LinearSearch():

    # Linear Search Main Page ( Overall sub page )
    print()
    print("Linear Search Sub Page")
    print()
    print("----------")
    print()
    print("Linear Search Integers: 1")
    print()
    print("Linear Search Strings: 2")
    print()
    print("Exit Program: 3")
    print()

    # Ask the user to enter his choice for linear search sub-page
    # Exception Handling
    try:

        # Ask the user to enter a choice for linear search sub-page
        choice_linear_search = int(input("Please Enter A Choice From The Above Choices: "))

    # If users anything character except of integers
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

    if choice_linear_search == 1:

        print("----------")
        print("Linear Search String")
        print("----------")

        # Calling the function "LinearSearch_Number" to allow user to search for value in array
        result_linear_number = LinearSearch_Number(num)

        # Output the "answer" of "LinearSearch_Number" in a appropriate message
        if result_linear_number != -1:

            # If "Linear_Input_Num" has been found
            print()
            print("Has been found at address: " + str(result_linear_number))
            print()

        else:

            # If "Linear_Input_Num" has NOT been found
            print()
            print("Has NOT been found!")
            print()

    elif choice_linear_search == 2:

        print("----------")
        print("Linear Search String")
        print("----------")

        # Calling the function "LinearSearch_String" to allow user to search for value in array
        result_linear_string = LinearSearch_String(anime)

        # Output the "answer" of "LinearSearch_String" in a appropriate message
        if result_linear_string != -1:

            # If "Linear_Input_Num" has been found

            print()
            print("Has been found at address: " + str(result_linear_string))
            print()

        else:

            # If "Linear_Input_Num" has NOT been found
            print()
            print("Has NOT been found!")
            print()

    else:

        # Exits program entirely
        print()
        print("Exiting Program")
        print()

        # Exits Program
        exit

# Function with identifier name "BinarySearch_Number" which will be used to allow the user to find a value in array "num"
def BinarySearch_Number(num, Binary_Input_Number):

    # It will return the function "BinarySearch_Number_Calc" which perform the "searching" function
    return BinarySearch_Number_Calc(num, 0, len(num), Binary_Input_Number)

def BinarySearch_Number_Calc(num, lower, upper, Binary_Input_Number):

    # Condition to enter "while" loop
    while lower <= upper:

        # Calculate the middle ( address ) of array "num"
        mid = (lower + upper) // 2

        # Searching for the value
        if num[mid] == Binary_Input_Number:

            # It will return the address of the searched value
            return mid

        # If value to search is NOT found
        # If value to be found is less than the value at mid
        elif num[mid] < Binary_Input_Number:

            # Cuts the BOTTOM half of the array
            # Only upper part is now left
            lower= mid + 1

        else:

            # Cut the TOP half of the array as
            # value to be found is greater than the value at mid
            # Only lower part is not left
            upper = mid - 1

    # If "Binary_Input_Number" has not been found
    return - 1

# Function with identifier name "BinarySearch_String" which will be used to allow the user to find a value in array "anime"
def BinarySearch_String(anime, Binary_Input_String):

    # It will return the function "BinarySearch_Number_Calc" which perform the "searching" function
    return BinarySearch_String_Calc(anime, 0, len(num), Binary_Input_String)

def BinarySearch_String_Calc(anime, lower, upper, Binary_Input_String):

    # Condition to enter "while" loop
    while lower <= upper:

        # Calculate the middle ( address ) of array "anime"
        mid = (lower + upper) // 2

        # Searching for the value
        if anime[mid] == Binary_Input_String:

            # It will return the address of the searched value
            return mid

        # If value to search is NOT found
        # If value to be found is less than the value at mid
        elif anime[mid] < Binary_Input_String:

            # Cuts the BOTTOM half of the array
            # Only upper part is now left
            lower= mid + 1

        else:

            # Cut the TOP half of the array as
            # value to be found is greater than the value at mid
            # Only lower part is not left
            upper = mid - 1

    # If "Binary_Input_String" has not been found
    return - 1

# Binary Search ( Sub-Page )
# Function with identifier name "BinarySearch" will be our sub page ( for binary search )
def BinarySearch():

    # Binary Search Main Page ( Overall sub page )
    print()
    print("Binary Search Sub Page")
    print()
    print("----------")
    print()
    print("Binary Search Integers: 1")
    print()
    print("Binary Search Strings: 2")
    print()
    print("Exit Program: 3")
    print()

    # Exception Handling
    try:

        # Ask the user to enter a choice for binary search sub-page
        choice_binary_search = int(input("Please Enter A Choice From The Above Choices: "))

    # If users anything character except of integers

    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()    

    if choice_binary_search == 1:

        print("----------")
        print("Binary Search String")
        print("----------")

        # Remember, the array need to be sorted for binary search to work
        BubbleSort_Number(num)

        # Exception Handling
        try:

            # Displaying a little message so that the programmer writing this does not get lost
            print()
            print("User!, This is for Binary Search for Numbers")
            print()

            # Asking the user to enter a value to find in array "num"
            Binary_Input_Number = int(input("Please Enter A Value To Search: "))

        # If user enter any character other than integer values
        except ValueError:

            # Outputs appropriate message
            print()
            print("Please Enter Integer Values Only")
            print()

        # Calling the function "BinarySearch_Number" to allow user to search for value in array
        result_binary_number = BinarySearch_Number(num, Binary_Input_Number)

        # Output the "answer" of "LinearSearch_Number" in a appropriate message
        if result_binary_number != -1:

            # If "Binary_Input_Num" has been found
            print()
            print(str(Binary_Input_Number) + " has been found at address: " + str(result_binary_number))
            print()

        else:

            # If "Binary_Input_Num" has NOT been found
            print()
            print("Has NOT been found!")
            print()

    elif choice_binary_search == 2:

        print("----------")
        print("Binary Search String")
        print("----------")

        # Remember, the array need to be sorted for binary search to work
        BubbleSort_Anime(anime)

        # Exception Handling
        try:

            # Displaying a little message so that the programmer writing this does not get lost
            print()
            print("User!, This is for Binary Search for Strings")
            print()

            # Asking the user to enter a value to find in array "num"
            Binary_Input_String = str(input("Please Enter A Value To Search: "))

        # If user enter any character other than integer values
        except ValueError:

            # Outputs appropriate message
            print()
            print("Please Enter Integer Values Only")
            print()

        # Calling the function "LinearSearch_String" to allow user to search for value in array
        result_binary_string = BinarySearch_String(anime, Binary_Input_String)

        # Output the "answer" of "BinarySearch_String" in a appropriate message
        if result_binary_string != -1:

            # If "Binary_Input_Num" has been found
            print()
            print("Has been found at address: " + str(result_binary_string))
            print()

        else:

            # If "Binary_Input_Num" has NOT been found
            print()
            print("Has NOT been found!")
            print()

    else:

        # Exits program entirely
        print()
        print("Exiting Program")
        print()

        # Exits Program
        exit

# Start Of Program
# Main Program ( Main Page )

print("Computer Science Programming Project")
print()
print("Main Page")
print()
print("----------")
print()
print("Please Select From The Choices Below!")
print()
print("----------")
print()
print("Insertion Sort: 1")
print()
print("Bubble Sort: 2")
print()
print("Binary Search: 3")
print()
print("Linear Search: 4")
print()
print("Exit Program: 5")
print()

# Asking the user to enter a choice ( chooses from above )
# Exception Handling
try:

    # Ask the user to enter his "choice"
    choice = int(input("Please Enter A Choice From The Above Choices: "))

# If user enters anything else other than integer characters
except ValueError:

    # Outputs appropriate values
    print()
    print("Please Enter Integer Values Only!")
    print()

# Program Will Provide Corresponding Respond To User Choice
# User chooses "Insertion Sort"
if choice == 1:

    InsertionSort()

# User chooses "Bubble Sort"
elif choice == 2:

    BubbleSort()

# User chooses "Binary Search"
elif choice == 3:

    BinarySearch()

# User chooses "Linear Search"
elif choice == 4:

    LinearSearch()

elif choice == 5:

    # Exits program entirely
    print()
    print("Exiting Program")
    print()

    # Exits Program
    exit

else:

    print()
    print("Something Went Wrong!")
    print()

```

---

# Code 2:

This code will ask the *user* to enter a **name**. The program will then:

1. Displays "*name*" in slow motion
2. Displays "*name*" in slow motion and also in reversed order

Date Given: 23th September 2023
Date Completed: 23th September 2023

```python

# Random Program Code 2

# Importing Module Time
import time

# Global Variable "seconds"
# DECLARE seconds: OF REAL
global seconds

# Initialising seconds with a value
seconds = 0.5

# Ask the user to enter his name
print()
# DECLARE name: OF STRING
name = str(input("Please Enter A Name: "))
print()

# Function with identifier name "ascending_order"
# FUNCTION ascending_order(name) RETURNS String
def ascending_order(name):

    # Displaying Each Letter in "name"
    for x in name:

        # end="" --> Prints the value on the same line
        # flush=True --> Does not keep value in buffer and outputs the value as soon as it gets it
        print(x,end="", flush=True)

        # Will wait "0.5" seconds before displaying next letter
        time.sleep(seconds)

# Making the user's name in reversed order ( backwards )
# DECLARE backwards: OF STRING
# [start( inclusive ):stop( exclusive ):step]
backwards = str(name[::-1])

# Function with identifier name "descending_order"
# FUNCTION descending_order(backwards) RETURNS STRING
def descending_order(backwards):

    # Displaying Each Letter in "backwards"
    for x in backwards:

        # end="" --> Prints the value on the same line
        # flush=True --> Does not keep value in buffer and outputs the value as soon as it gets it
        print(x,end="", flush=True)

        # Will wait "0.5" seconds before displaying next letter
        time.sleep(seconds)

# Calling Function
print("Displaying Name ( NORMAL ORDER )")

# Called Function "ascending_order"
ascending_order(name)

print()
print()

print("Displaying Name ( NORMAL ORDER )")

# Called Function "descending_order"
descending_order(backwards)

print()
print()

```

---

# Code 3:

This program will allow to the user to *summon* a random number. Could be use to play:

- Snakes and Ladder
- "*Ludo*"
- And More

Date Started: 15th October 2023
Date Completed: 15th October 2023

```python

# Importing "random" Module
import random

print()
print("Snakes and Ladder | Ludo | ETC")
print()

print("1 Die")

# Displaying 1 Random Numbers
print("Your Number Is: " + str(random.randint(1, 6)))

print()
print()

print("2 Dice")

# DECLARE num_1: OF STRING
num_1 = random.randint(1, 6)

# DECLARE num_2: OF STRING
num_2 = random.randint(1, 6)

# DECLARE total: OF STRING
total = num_1 + num_2

# Displaying Output
print("Number 1 : " + str(num_1))
print("Number 2 : " + str(num_2))
print("Total: " + str(total))

print()

```

---

# Code 4:

This code is basically a Rock, Paper, Scissors Game

```python

# Rock Paper Scissors

# Importing "random" Module
import random

print()

# DECLARE array: ARRAY[2] OF INTEGER
array = ["rock", "paper", "scissors"]

# Displaying Output
print("Output: " + str(random.choice(array)))

```

Date Started: 15th October 2023
Date Completed: 15th October 2023

---

# Code 5:

This code is a simple calculator that will ask the user to input 2 number from the user and perform some calculation that the user has chose

```python

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
    print(f"Real Answer = {total}")
    print()
    print(f"Positive Answer = {positive_value}")

# Function with identifier name "sub" will subtract the number
def sub(x, y):

    # Performing Subtraction
    answer = x - y
    negative_value = y - x

    # Displaying the results
    print(f"Real Answer = {answer}")
    print()
    print(f"Negative Answer = {negative_value}")

# Function with identifier name "multiply" will perform multiplication on the numbers
def multiply(x, y):

    # Performing Multiplication
    positive_value = abs(x * y)
    negative_value = x * y

    # Displaying the results
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
                add(num1, num2)

            # Subtraction
            case 2:

                # Calling Function inside the "main_calc" function
                insert_values()
                sub(num1, num2)

            # Multiplication
            case 3:

                # Calling Function inside the "main_calc" function
                insert_values()
                multiply(num1, num2)

            # Division
            case 4:

                # Calling Function inside the "main_calc" function
                insert_values()
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

```

>[!note]
>I had some problem initially where even though I wrote
>```python
>global num1
>global num2
>```
>They still did not work
>>[!tip] Fix
>>- I found out that you need to declare the variables first and then it can be used from one function to the next
>>- You also need to write,
>> ```python
>>global num1
>>global num2
>> ```
>>- **again** in the *insert_values* function as the values are changing
>>- Think of it like passing by **REFERENCE**; do me a favour, just read the code above (  )


# Code 6

Better Rock, Paper, Scissor game than [[Random HSC Python Codes#Code 4 | this crap]].

```python

import random

print()

rpc = ["rock", "paper", "scissors"]

# Ask the user to enter his name
user_name = input("Please Enter You Name: ")

# Ask the user to enter a choice
user_choice = input("Please Enter A Choice: ")

# Computer Gets a randomly selected choice
computer_choice = random.choice(rpc)

print(f"User's Choice: {user_choice}")
print(f"Computer's Choice: {computer_choice}")

# Condition to Tie

# user = rock | computer = rock
# user = scissors | computer = scissors
# user = paper | computer = paper

if user_choice == computer_choice:

    print()
    print("Tie")
    print()

# Conditions to win

# user = rock | computer = scissors ---> user wins
# user = paper | computer = rock ---> user wins
# user = scissors | computer = paper ---> user wins

if ((user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper")):

    print()
    print(f"{user_name} Wins")
    print()

# user = paper | computer = scissors ---> computer wins
# user = rock | computer = paper ---> computer wins
# user = scissors | computer = rock ---> computer wins

elif ((user_choice == "paper" and computer_choice == "scissors") or (user_choice == "rock" and computer_choice == "paper") or (user_choice == "scissors" and computer_choice == "rock")):

    print()
    print("Computer Wins")
    print()


```

# Code 7

This is a simple Palindrome Checker.

```python

# Intiailly variable user_input is equal to nothing i.e ""
user_input = ""

print()

# Let user input a string
# Will continue to ask user to enter data until user inputs something
while user_input == "":

    user_input = input("Please Enter A String: ")

    # If user types "exit" ---> Program will exit
    if user_input == "exit":

        exit()

# Find the reverse of user_input
reversed_string = user_input[::-1]

# Finding Palindrome

# Check if user_input == reversed_string
if user_input == reversed_string:

    print()
    print(f"{user_input} is a Palindrome")

    # Exits the program
    exit()

else:

    print()
    print(f"{user_input} is not a Palidrome")

    # Exits the program
    exit()

```

---

# Code 8

This will allow the user to generate a password in his desired length

>[!note]
>At this point in time; I have not yet learned any [[Modules - Python | modules]] in Python.
>I do not really understand the `string` module for now.
>But I did check the [documentation]()

>[!bug] Warning
>If you are actually making a password generator for real life use. BE CAREFUL...
>The user does not see the code and the code might be writing all the password behind in a file!

```python

# Importing Modules

# `random` module allows for random choosing of characters
import random
# `string` modules allows for `join` function
import string

print()
number = int(input("Please Enter Length of Password: "))
print()

# Choice of characters from letters to digits to symbols
    # Check docs link
pass_chars = string.ascii_letters + string.digits + string.punctuation

# Creating the actual password
password = ''.join(random.choice(pass_chars) for x in range(number))

# Output the password to user
print(f"The password = {password}")
print()

```

## Code 8 ( my shitty version )

```python

# Import Modules
import string
import random

print()

# Variable `chars` will hold all the combination of letters, digits, punctuation
chars = string.ascii_letters + string.digits + string.punctuation

# Exception Handling
try:
    # Allow user to enter number
    user_input = int(input("Please Enter Length of Password: "))
    print()

    for x in range(user_input):
        print(random.choice(chars), end="", flush=True)

except ValueError:
    print()
    print("Please Enter Interger Numbers Only!")
    print()

print()

```

# Code 9

This is something that I wanted to do. This is something similar to an Urban Terminal Parking thing.

```python

array_main = [1, 2, 3, 4, 5]
array_unwanted = []

# Make a function to print the arrays
def output_arrays(array1, array2):

    print("Main Array")
    print()

    for x in array1:
        print(x)

    print()

    print("Unwanted Array")
    print()

    if not array2:

        print()
        print("Nothing In Array")
        print()

    else:

        for y in array2:
            print(y)

        print()

# Binary Search
def binarysearch(array, userinput):
    # calls the function that performs the calculation
    return binarysearch_calc(array, 0, len(array) - 1, userinput)


# Function that performs the binary search calcuation
def binarysearch_calc(array, lower, upper, userinput):
    while lower <= upper:
        mid = (lower + upper) // 2

        if array[mid] == userinput:
            return mid

        elif array[mid] < userinput:
            lower = mid + 1

        elif array[mid] > userinput:
            upper = mid - 1

    return -1


# Main Function
def main():

    print()
    # Ask the user to input a value
    user_input = int(input("Please Enter A Value: "))

    # Check if whether the the value entered by number already is in main array
    result = binarysearch(array_main, user_input)

    # if number does not exist in main array
    if result == -1:

        # Add user input to main array
        array_main.append(user_input)
        print()
        print("Value Added")
        print()

    # if number exist in main array
    else:

        # will add this to the unwanted array
        array_unwanted.append(user_input)
        print()
        print("Your Value Has Already Been Added")
        print()

# Calling Functions to test
main()

output_arrays(array_main, array_unwanted)


```

# Code 10

This is a simple code that will calculate the average of the numbers in an array.

It will include 2 "*methods*":

1. Finding the `total` manually
2. Using the `sum()` function to find the *total*

The YouTuber [The Coding Sloth](https://www.youtube.com/watch?v=SS19Q-_saCc) made a video about how coding is hard. He said to find the average of some numbers in an array without using the function `sum()`; so I did it ( *by myself $\rightarrow$ need to put that here because I am fool and cannot program* )

>Today is the 27 of March of 2024 @ 13:56
>The more I code in C, the more I lose Confidence.

```Python

# DECLARE ARRAY numbers: INTEGER
numbers = [1, 2, 3, 4, 5]
# DECLARE array_size: INTEGER
array_size = len(numbers)
# DECLARE total: INTEGER
global total

# FUNCTION avg1()
def avg1():

    total = 0
    # Calculate the Total of the Numbers in Array
    for x in range(array_size):

        # DECLARE num: INTEGER
        num = numbers[x]
        total = total + num

    # Calculate the Average
    # DECLARE average1: INTEGER
    average1 = total / array_size

    # Output the Average
    print(f"Average ( Method 1 ): {average1}")

# FUNCTION avg2()
def avg2():

    # DECLARE average2: INTEGER
        # Using `sum()` function
    average2 = sum(numbers) / array_size

    # Output the Average
    print(f"Average ( Method 2 ): {average2}")

print()
# Calling Functions
avg1()
print()
avg2()

```

---

# Socials

- [**GitHub**](https://www.github.com/Sunhaloo)
- [**Instagram**](https://www.instagram.com/s.sunhaloo/)
- [**YouTube**](https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg)

---
Thank You!
