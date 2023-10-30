# Queue Program Code

# NOTE: The array starts at index 0

# DECLARE front: OF INTEGER
# Global pointer "front" will keep track to the first item ( added )
global front
# Pointer front has initial value of "-1"
front = -1
# DECLARE rear: OF INTEGER
# Global pointer "rear" will keep track of the last item ( added )
global rear
# Pointer r ear has initial value of "-1"
rear = -1
# DECLARE queue_length: OF INTEGER
# Global constant "queue_length" will keep 
# Constant "queue_length" will hold the "actual" length of array
queue_length = 5
# DECLARE queue: ARRAY[4] OF INTEGER
# Global array "queue" with length 5
queue = []
# FUNCTION display()
# Function "display" will be used to display our array
def display():
    # DECLARE x: OF INTEGER
    # "Using" our global variables
    global front
    global rear
    # If array is empty
    if not queue:
        # "front" and "rear" Pointers stay the same value
        print()
        print("Array is EMPTY")
        print()
        # Displaying Pointers
        print(f"Front Pointer ---> {front}")
        print(f"Rear Pointer ---> {rear}")
        print()
    # If array is NOT empty
    else:
        # Display value of array ( on separate lines )
        for x in queue:
            print(x)
        print()
        # Pointer "front" becomes:
        front = len(queue) -1
        # Pointer "rear" take the value "0"
        rear = 0
        # Displaying Pointers
        print(f"Front Pointer ---> {front}")
        print(f"Rear Pointer ---> {rear}")
        print()
# FUNCTION enqueue(BYVAL input_item: OF INTEGER)
# Function "enqueue" will allow the user to enter value in the array
def enqueue(input_item):
    # Using our global variables
    global rear
    global front
    global queue_length
    # Check if "queue" is full
    if rear == queue_length - 1:
        # Outputs appropriate message
        print()
        print("Array is already FULL!")
        print()
    # If array "queue" is NOT full
    else:
        # If front pointer is initially "-1"
            # Meaning that the array is COMPLETELY empty
        if front == -1:
            # Hence, if array was COMPLETLY empty in the beginning
            # Both pointer will go at index 0 when a value is entered
            front = rear = 0
        # If array "queue" was PARTIALLY empty
        else:
            # Pointer "rear" increases by 1
            rear += 1
        # Inserts element into queue
        queue.append(input_item)
# FUNCTION dequeue()
# Function "dequeue" will remove the first value ( added ) into "queue"
def dequeue():
    # Using our global variables
    global front
    global rear
    global queue_length
    # Check if "queue" is already empty
        # This is done by checking the length of array "queue"
    if queue_length == 0:
        # Pointer rear will become "-1"
        rear = -1
        # Outputs appropriate message
        print()
        print("Array is already EMPTY!")
        print()
    # If array "queue" is not empty
        # Could have also used "else" statement
        # For "explanation" sake; I used the "elif" statement
    elif rear >= 0:
        # Removes the first value ( added ) from array
        queue.pop(0)
        # Pointer "front" decreases by 1
        front -= 1
        # Variable / Constant needs to decrease by 1
        queue_length -= 1
# FUNCTION specific_delete(BYVAL input_item: OF INTEGER)
# Function "specific_delete" will allow the user to remove a "specific" element in the queue
def specific_delete(input_item):
    # Using our global variables
    global front
    global rear
    global queue_length
    # DECLARE array_length: OF INTEGER
    # Variable "array_length" will hold the length of "queue"
    array_length = len(queue) -1
    # Pointer "front" becomes
    front = len(queue) -1
    # Check if array "queue" is already empty
    if queue_length == 0:
        # Pointer "rear" becomes -1
        rear = -1
        # Outputs appropriate message
        print()
        print("Array is already EMPTY!")
        print()
    # If array "queue" is not empty
        # Could have just used "else" statement
        # For "explanation" sake; I will be using the "elif" statement
    elif rear >= 0:
        # DECLARE Found: OF BOOLEAN
        # Variable "Found" will change to "True" if our "input_item" has been Found
        Found = False
        # Stepping through array to find value
        for x in range(array_length):
            # If value has been found
            if queue[x] == input_item:
                # Variable "Found" will become "True"
                Found = True
                # Removing that specific value
                queue.remove(queue[x])
                # Outputs a message
                print(f"{input_item} has been removed")
                print()
                # Pointer "front" will decreases by 1
                front -= 1
                # Variable / Constant "queue_length" will decrease by 1
                queue_length -= 1
                # Breaking away from "FOR" loop
                break
        # If "input_item" has NOT been found
        if not Found:
            # Outputs appropriate message
            print()
            print(f"{input_item} has NOT been found")
            print()
# FUNCTION bubble_sort()
# Function "bubble_sort" will sort the array in ASCENDING ORDER
    # Ascending Order; because "binary search" needs the array in Ascending Order
def bubble_sort():
    # DECLARE update: OF BOOLEAN
    # Variable "update" will become "True" if values have been swapped
    update = True
    # DECLARE swap: OF INTEGER
    # Variable "swap" will increment after each time a value has been swapped
    swap = 0
    # DECLARE array_length: OF INTEGER
    # Constant "array_length" will hold the length of array "queue"
    array_length = len(queue)
    # DECLARE temp: OF INTEGER
    # Variable "temp" will acts as a temporary "buffer" / "register"
        # Temporarily holding our value being swapped
    # Condition to enter "WHILE" loop
    while update == True and array_length > 0:
        # Variable "update" will become "False"
            # So that it can be "updated" after a swap
        update = False
        # Number of times it will enter array
        for x in range(0, array_length -1):
            # Number of time it will swap values
            for y in range(0, array_length -1):
                # Sorting in ASCENDING ORDER
                if queue[y] > queue[y + 1]:
                    # Swapping Part
                    temp = queue[y]
                    queue[y] = queue[y + 1]
                    queue[y + 1] = temp
                    # Variable "update" becomes "True"
                    update = True
                    # Variable "swap" will increases by 1
                    swap += 1
# FUNCTION insertion_sort()
# Function "insertion_sort" will sort the array in ASCENDING ORDER
    # Ascending Order; because "binary search" needs the array to be in Ascending Order
def insertion_sort():
    # DECLARE array_length: OF INTEGER
    # Variable "array_length" will hold the length of array "queue"
    array_length = len(queue)
    # Stepping through array
    for x in range(1, array_length):
        # DECLARE values: OF INTEGER
        # Variable "values" will hold the values at index x
        values = queue[x]
        # DECLARE y: OF INTEGER
        # Variables "y" will hold the index to the left of "x"
        y = x -1
        # Condition to enter "WHILE" loop
        while y >= 0 and queue[y] > values:
            # Swapping Part
            queue[y + 1] = queue[y]
            # Variable "y" decreases by 1
            y -= 1
        # If array is already sorted
        queue[y + 1] = values
# FUNCTION l_search(BYVAL search_item: OF INTEGER)
# Function "l_search" will allow the user to search for an item in the array
def l_search(search_item):
    # DECLARE array_length: OF INTEGER
    # Variable "array_length" will hold the length of array "queue"
    array_length = len(queue)
    # Stepping through the array
    for x in range(array_length):
        # If value has been found
        if queue[x] == search_item:
            # Returns the address of the search value
            return x
    # If "search_item" has NOT been found
    return -1
# FUNCTION display_linear(BYVAL result: OF INTEGER)
# Function "display_linear" will allow the user to display the result of linear search
def display_linear(result):
    # If "search_item" has been found
    if result != -1:
        # Outputs the appropriate message
        print()
        print(f"Value is found at address: {result}")
        print()
    # If "search_item" has NOT been found
    else:
        # Output appropriate message
        print()
        print("Value has not been found")
        print()
# FUNCTION b_search(BYVAL search_item, BYVAL array: OF INTEGER)
# Function "binary search" will allow the user to search for a value in array
def b_search(array, search_item):
    # Returns the function "b_search_calc"
    return b_search_calc(0, len(array)-1, array, search_item)
# FUNCTION b_serach_calc(BYVAL array: OF INTEGER, BYVAL search_item: OF INTEGER)
# Funtion "b_search_calc" will be the one responsible
    # for performing our binary search calculations
def b_search_calc(lower, upper, queue, search_item):
    # Condition to enter "WHILE" loop
    while lower <= upper:
        # DECLARE mid: OF INTEGER
        # Variable "mid" will be used to calculate our array
        mid = (lower + upper) // 2
        # Searching for our value
        if queue[mid] == search_item:
            # Returns the address of "search_item"
            return mid
        # If value is found in the upper part of array
        elif queue[mid] < search_item:
            # Variable "lower" takes the index just after mid
            lower = mid +1
        # If value is found in the lower part of array
        else:
            # Variable "upper" take the index just before mid
            upper = mid -1
# FUNCTION display_binary(BYVAL result: OF INTEGER)
# Function "display_binary" will allow the user to display the result of binary search
def display_binary(result):
    # If "search_item" has been found
    if result != -1:
        # Outputs the appropriate message
        print()
        print(f"Value is found at address: {result}")
        print()
    # If "search_item" has NOT been found
    else:
        # Output appropriate message
        print()
        print("Value has not been found")
        print()
# Calling Functions
# Displaying Initial Array
print()
print("Displaying Empty Array")
display()
# Inserting Items
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
# This will cause an error
print("Obviously cannot add 6th item")
enqueue(6)
# Displaying array After inserting values
print()
print("Displaying array After inserting values")
display()
# Removing 2 "first" values
print()
print("Removing 2 'first' value")
dequeue()
dequeue()
# Displaying array After removing first 2 values
print()
print("Displaying array After removing 2 'first' values")
display()
# NOTE: An error is occuring at this point
    # I cannot add more items
    # Even though the array in not full, I cannot add more items
enqueue(2)
# Deleting a specific value from array
specific_delete(4)
# Displaying array after calling "specific_delete"
print()
print("Displaying array after calling 'specific_delete'")
display()
# Sorting the array in Ascending Order
print()
print("Sorting the array in Ascending Order")
bubble_sort()
# Uncomment "insertion_sort()" and comment "bubble_sort()"
    # to use insertion sort instead of bubble sort
#insertion_sort()
# Displaying array after sorting
print()
print("Displaying the array after sorting")
display()
# Performing linear search
# Finding the number "2"
result_linear = l_search(2)
print()
print("Displaying array After applying Linear Search")
display_linear(result_linear)
# Performing binary search
# Finding the number "5"
result_binary = b_search(queue, 5)
print()
print("Displaying array After applying Binary Search")
display_binary(result_binary)
# Displaying array
print()
print("Displaying array for one last time")
display()
