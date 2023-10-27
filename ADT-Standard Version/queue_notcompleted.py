# Queue Program Code

# DECLARE front: OF INTEGER
# Global pointer "front" will keep track of the first item
global front

# DECLARE rear: OF INTEGER
# Global pointer "rear" will keep track of the last item
global rear

# DECLARE queue_length: OF INTEGER
# Global constant which will keep the length of array queue
queue_length = 5

# DECLARE queue: ARRAY[4] OF INTEGER
# Our 1D-Array with identifier name "queue"
queue = []

# FUNCTION display_array(BYVAL array: ARRAY[4] OF INTEGER) RETURNS INTEGER
# Function "display_array" which will display any array
def display(array):

    # DECLARE x: OF INTEGER
    # Variable "x" is a counter that will be used to display our values in "array"

    # "calling/using" our global pointers
    global front
    global rear

    # Pointer "front" becomes -1
    front = -1
    # Pointer "rear" becomes -1
    rear = -1

    # If array is EMPTY
    if not array:
        
        # Outputs appropriate message
        print()
        print("Array is EMPTY")
        print()

        # Displaying pointers
        print()
        # Pointer "front" will stay at "-1"
        print(f"Front Pointer ---> {front}")
        # Pointer "rear" will stay at "-1"
        print(f"Rear Pointer ---> {rear}")
        print()

    # If array is NOT EMPTY
    else:

        # Pointer "front" becomes
        front = len(array) -1
        # Pointer "rear" stays "0"
        rear = 0

        print()
        print("Displaying Array")

        # Displaying array ( values on separate lines )
        for x in array:

            print(x)

        # Displaying pointer's "location"
        print()
        print(f"Front Pointer ---> {front}")
        print(f"Rear Pointer ---> {rear}")
        print()

# FUNCTION enqueue(BYVAL item: OF INTEGER, BYVAL array: ARRAY[4] OF INTEGER)
# Function "enqueue" will allow us to insert elements in array
def enqueue(item, array):

    # "Calling"/"using" global variables and constants
    global front
    global queue_length

    # Pointer "front" becomes
    front = len(array) - 1

    # Check if array is full
    if front == queue_length - 1:

        print()
        print("Array is FULL!")
        print()

    # If array is NOT empty
    elif front < queue_length -1:

        # Pointer "front" increases by 1
        front += 1

        # "Inserts" the item at index 0
            # Because FIFO, first item, need to be the first one out
        array.insert(0, item)

# FUNCTION dequeue(item, array)
# Function "dequeue" will remove the first value added to queue
    # In this function we will be using "pop" function
    # If we used "append" function to insert values
        # We would need to use "pop(0)" to remove the value
# NOTE: This fucntion is bad \_(-_-)_/
def dequeue(array):

    # "Calling"/"using" our global variables and constants
    global front
    global rear
    global queue_length

    # Check if array is Empty
    if queue_length == 0:

        # Pointer "rear" becomes "-1"
        rear = -1

        print()
        print("Array is already EMPTY!")
        print()

    else:

        # Removes first item ( added ) from array
        array.pop()
        # Pointer "front" decreases by 1
        front -= 1
        # Constant / Variable "queue_length" will decreases by 1
            # Length of array decreases as number of elements in the array decreases
        queue_length -= 1

# FUNCTION specific_delete()
# Function "specific_delete" will remove a value found in the array
def specific_delete(item, array):

    # "Calling"/"using" our global constants and variables
    global front
    global rear
    global queue_length

    # Check if array is alredy empty
    if queue_length == 0:

        print()
        print("Array is already EMPTY")
        print()

    else:

        print("pass")

# Calling Function
display(queue)



display(queue)

specific_delete(5, queue)

display(queue)
