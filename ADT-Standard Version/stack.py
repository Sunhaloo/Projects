# Stack Program Code

# DECLARE top: OF INTEGER
# Global pointer "top" will keep track of the last item added
global top

# DECLARE base: OF INTEGER
# Global pointer "base" will be used to check if array is empty
global base

# DECLARE stack: ARRAY[4] OF INTEGER
# Our 1D-Array with identifier name "stack"
stack = [9, 22, 4]

# Functions

# FUNCTION display_array RETURNS INTEGER
# Function "display_array" which will display our "stack"
def display_array():

    # DECLARE x: OF INTEGER
    # Variable "x" is a counter that will be used to display our values in "stack"

    # If array is EMPTY
    if not stack:

        # Pointer "top" become "-1"
        top = -1

        # Ponter "base" becomes 0
        base = 0
        
        # Displays appropriate message
        print()
        print("Array is EMPTY")

        # Displaying pointer top "location"        
        print()
        print(f"Top Pointer ---> {top}")
        print(f"Base Pointer ---> {base}")
        print()

    # If array is NOT empty
    else:
        # Pointer "top" becomes
        top = len(stack) -1
        # Pointer "base" stays 0
        base = 0

        print()
        print("Displaying Array")

        # Displaying array "stack" ( values on separate lines )
        for x in stack:
            print(x)

        # Diplaying pointer top "location"
        print()
        print(f"Top Pointer ---> {top}")
        print(f"Base Pointer ---> {base}")
        print()

# FUNCTION insert_value_top(BYVAL input_item: OF INTEGER)
# Function "insert_value" will allow us to insert elements in array
def insert_value_mine(input_item):

    # DECLARE array_length: OF INTEGER
    # Variable "array_length" will hold the length of array
        # NOTE: Do not use "len(array)"; programmer need to write the length of array
    array_length = 5

    # Pointer "top" will hold the index of last item in array "stack"
    top = len(stack) -1

    # Temporary Holder for top
    top_1 = top + 1

    # Check if array is full
    if (top_1) == array_length:

        # Outputs appropriate message
        print()
        print("Array is FULL!")
        print()
    # If array "stack" in NOT full
    
    elif (top_1) < array_length:

        # Pointer "top" increases by 1
        top_1 += 1

        # "Appends" the item to the "stack"
        stack.append(input_item)

# The function "insert_value" below is a better version of the above function "insert_value_top"
# FUNCTION insert_value(BYVAL input_item: OF INTEGER)
# Function with identifier name "insert_value" will allow us to insert elements in array

def insert_value(input_item):

    # DECLARE array_length: OF INTEGER
    # Variable "array_length" will hold the length of array
        # NOTE: Do not use "len(array)"; programmer need to write the length of array
    array_length = 5

    # Pointer "top" will hold the index of last item in array "stack"
    top = len(stack) -1

    # Check if array is full
    if top == array_length -1:

        # Outputs appropriate message
        print()
        print("Array is FULL!")
        print()

    # If array "stack" is NOT full
    elif top < array_length -1:

        # Pointer "top" increases by 1
        top += 1

        # "Appends" the item to the "stack"
        stack.append(input_item)

# FUNCTION pop_value()
# Function "pop_value()" will remove the last value ( added ) from "stack"
def pop_value():

    # Pointer "top" will keep of index of last item in "stack"
    top = len(stack) -1

    # Pointer "base" will keep track of the "lower bound" of array
    base = 0
    
    # Check if "stack" is already EMPTY
    if top == base - 1:

        # Outputs appropriate message
        print()
        print("Array Is Already EMPTY!")
        print()

    # If array is NOT emtpy
    else:

        # Pointer "top" decreases by 1
        top -= 1

        # Removes the last value ( added ) from "stack"
        stack.pop()

# FUNCTION pop_values_mine
# Function "pop_value_mine" will remove the last value ( added )
def pop_values_mine():

    # Pointer "top" will keep of index of last item in "stack"
    top = len(stack) -1
    
    # Pointer "base" will keep track of the "lower bound" of array
    base = 0

    # Check if array is NOT empty
        # Thus, if array is not empty, we can remove values
    if top >= 0:

        # Pointer "top" decreases by 1
        top -= 1

        # removes value
        stack.pop()

    # If array "stack" is EMPTY
    elif top == base -1:

        # Output appropriate values
        print()
        print("Array Is Already EMPTY!")
        print()

# FUNCTION specific_delete(BYVAL delete_item)
# Function "specific_delete" will remove a specific value from "stack"
def specific_delete(delete_item):

    # DECLARE x: OF INTEGER

    # DECLARE found: OF BOOLEAN
    # Constant "found" will become "True" is value to be removed has been found
    found = False

    # DECLARE array_length: OF INTEGER
    # Constannt "array_length" will hold the length of "stack"
    array_length = len(stack)

    # Pointer "top" will keep track of the last value ( added )
    top = len(stack) -1

    # Pointer "base" will keep track of the "lower bound" of array
    base = 0

    # Check if array "stack" is alredy EMPTY
    if top == base -1:

        # Outputs appropriate message
        print()
        print("Array is already EMPTY")
        print()

    # If array "stack" is NOT Emtpy
    else:

        # Steps through the array "stack"
        for x in range(array_length):

            # If value has been found
            if stack[x] == delete_item:

                # Variable "found" becomes "True"
                found = True

                # Removes value from "stack"
                stack.remove(stack[x])

                # Pointer "top" decreases by 1
                top -= 1

                # Exits "FOR" Loop
                break

        # If value has NOT been found
        if not found:

            # Outputs appropriate message
            print()
            print(f"{delete_item} Has NOT Been Found")
            print()

# FUNCTION bubble_sort()
# Function "bubble_sort" will sort the array in ASCENDING ORDER
    # Ascending Order; because Binary Search will need the array to be in ASC Order
def bubble_sort():

    # DECLARE temp: OF INTEGEr
    # Variable "temp" will store our values being swapped

    # DECLARE swaps: OF INTEGER
    # Variable "swaps" will count how many times values have been swapped
    swaps = 0

    # DECLARE update: OF BOOLEAN
    # Variable "update" will become "True" when values have been swapped
    update = True

    # DECLARE array_length: OF INTEGER
    # Constant "array_length" will hold the length of array
    array_length = len(stack)

    # Condition to enter "WHILE" Loop
    while update == True and array_length > 0:

        # Variable "update" will become False
            # So that I can become true later
        update = False

        # Number of times if will perform "bubble sort"
        for x in range(0, array_length -1):

            #  Number of time it will swap value
            for y in range(0, array_length -1):

                # Sorting in Ascending Order
                if stack[y] > stack[y + 1]:

                    # Swapping Part
                    temp = stack[y]
                    stack[y] = stack[y + 1]
                    stack[y + 1] = temp

                    # Variable "update" becomes "True"
                    update = True

                    # Variable "swaps" increases by 1
                    swaps += 1

# FUNCTION insertion_sort()
# Function "insertion_sort" will sort our array in ASCENDING ORDER
    # Ascending Order; because Binary Search will need the array to be in ASC Order
def insertion_sort():

    # DECLARE x: OF INTEGER

    # DECLARE array_length: OF INTEGER
    # Variable array_length will keep track of length of array
    array_length = len(stack)

    # Stepping through array
    for x in range(1, array_length):

        # DECLARE values: OF INTEGER
        # Variable "values" will hold the values at index "x"
        values = stack[x]

        # DECLARE y: OF INTEGER
        # Variable "y" will keep the index next to "x"
        y = x -1

        # Condition to enter "WHILE" loop
        while y >= 0 and stack[y] > values:
            
            # Swapping Part
            stack[y + 1] = stack[y]

            # Variable "y" decreases by 1
            y -= 1

        # If "stack" is already sorted
        stack[y + 1] = values

# FUNCTION linear_search(BYVAL search_item: OF INTEGER):
# Function "linear_search" will allow us to search a value in the array
def linear_search(search_item):

    # DECLARE array_length: OF INTEGER
    # Constant "array_length" will hold the length of "stack"
    array_length = len(stack)

    # Stepping through "stack"
        # Searching for "search_item"
    for x in range(0, array_length):

        # If "search_item" has been found
        if stack[x] == search_item:

            # Returns the address of "search_item"
            return x
        
    # If "search_item" has not been found
    return -1

# FUNCTION binary_search(BYVAL search_item: OF INTEGER):
# Function "binary_search" will allow us to search a value in the array
    # NOTE: We need to sort our array in ASCENDING ORDER for "binary_search" to work
def binary_search(search_item):

    # FUNCTION binary_search_calc(BYVAL stack, BYVAL 0, BYVAL LENGTH(stack) - 1, BYVAL search_item )
    # Function "binary_search_calc" will be the one to perform the calculation
    return binary_search_calc(stack, 0, len(stack) - 1, search_item)

# FUNCTION binary_search_calc(BYVAL stack, BYVAL 0, BYVAL LENGTH(stack) - 1, BYVAL search_item )
# Function "binary_search_calc" will be the one to perform the calculation
def binary_search_calc(stack, lower, upper, search_item):

    # Condition to enter "WHILE" Loop
    while lower <= upper:

        # DECLARE mid: OF INTEGER
        # Variable "mid" will find the middle of "stack"
        mid = (lower + upper) // 2

        # Finding the value

        # If value is found found in the middle
        if stack[mid] == search_item:

            # Returns the address of "search_item"
            return mid
        
        # If value at mid-pt is < search value
        elif stack[mid] < lower:

            # Discards the bottom part of array
            lower = mid + 1

        # If value at mid-pt is > search value
        else:

            # Discards the upper part of array
            upper = mid -1

# Calling Functions

print()
print("Displaying Initial Array")
display_array()

# Inserting Values
print()
print("Inserting Values")
print()

# Inserting values individually
insert_value(3)
insert_value(5)
# Value "90" will not be added to the array
insert_value(90)

print()
print("Displaying Array After Inserting Value")
display_array()

# "Popping Values"
print()
print("Removing Last Values ( Twice )")

# Both of these function below will remove the last value ( added ) into array
pop_values_mine()
pop_value()

print()
print("Displaying Array After Removing 2 Values")
display_array()

print()
print("Deleting -1")

# Trys to delete "-1"
    # Which is obviously going to return "-1" ---> Not Found
specific_delete(-1)

print()
print("Sorting Array")

# Sorts the "stack" in Ascending Order
bubble_sort()

# "Un-Comment" "insertion_sort()" to use insertion sort

#insertion_sort()

print()
print("Displaying Array After Sorting In Ascending Order")
display_array()

# Linear Search
result_linear = linear_search(22)

# FUNCTION display_linear(BYVAL result_linear: OF INTEGER)
# Function "display_linear" will display the result of function "linear_search"
def display_linear(result_linear):

    # If "search_item" has been found
    if result_linear != -1:

        # Outputs the appropriate =message
        print()
        print(f"Value Is Found At Address: {result_linear}")
        print()

    # If "search_item" has NOT been found
    else:

        # Outputs the appropriate =message
        print()
        print("Value Has NOT Been Found")
        print()

# Calling the function "display_linear"
display_linear(result_linear)

# Binary Search
result_binary = binary_search(9)

# FUNCTION display_binary(BYVAL result_binary: OF INTEGER)
# Function "display_binary" will display the result of function "binary_search"
def display_binary(result_binary):

    # If "search_item" has been found
    if result_binary != -1:

        # Outputs the appropriate message
        print()
        print(f"Value Is Found At Address: {result_binary}")
        print()

    # If "search_item" has NOT been found
    else:

        # Outputs the appropriate message
        print()
        print("Value Has NOT Been Found")
        print()

# Calling the function "display_binary"
display_binary(result_binary)

# S.Sunhaloo
