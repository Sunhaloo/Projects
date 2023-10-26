---
Alias: Queue FIFO
Tag: python, ADT, 1D-Array
Author: S.Sunhaloo
Type: ADT
Date: 2023-09-01
Status: Completed
---

## List of Contents

- [[Queue ADT - 1D Array ( Mine )#What is a Queue?| What is a Queue?]]
- [[Queue ADT - 1D Array ( Mine )#Operations of Queue ADT| Operations of Queue ADT]]
	- [[Queue ADT - 1D Array ( Mine )#Enqueue Operation| Enqueue Operation]]
	- [[Queue ADT - 1D Array ( Mine )#Dequeue Operation| Dequeue Operation]]
- [[Queue ADT - 1D Array ( Mine )#Pointers| Pointers]]
- [[Queue ADT - 1D Array ( Mine )#Photo| How it works ( Photo )]]
- [[Queue ADT - 1D Array ( Mine )#Queue Program Code| Queue Program Code]]
	- [[Queue ADT - 1D Array ( Mine )#Functions| Functions]]
		- [[Queue ADT - 1D Array ( Mine )#Initialising our Queue| Initialising our Queue]]
		- [[Queue ADT - 1D Array ( Mine )#Displaying Array| Displaying Array]]
		- [[Queue ADT - 1D Array ( Mine )#Inserting Values| Inserting Values]]
		- [[Queue ADT - 1D Array ( Mine )#Pop Function| Pop Function]]
		- [[Queue ADT - 1D Array ( Mine )#Delete Specific Element| Deleting Specific Element]]
			- [[Queue ADT - 1D Array ( Mine )#With ONLY **For Loop**| FOR Loop]]
			- [[Queue ADT - 1D Array ( Mine )#With **While Loop**| WHILE Loop]]
		- [[Queue ADT - 1D Array ( Mine )#Bubble Sort| Bubble Sort]]
		- [[Queue ADT - 1D Array ( Mine )#Insertion Sort| Insertion Sort]]
		- [[Queue ADT - 1D Array ( Mine )#Linear Search| Linear Search]]
			- [[Queue ADT - 1D Array ( Mine )#Displaying the "*result*" of linear search| Displaying Result of Linear Search]]
		- [[Queue ADT - 1D Array ( Mine )#Binary Search| Binary Search]]
			- [[Queue ADT - 1D Array ( Mine )#Displaying the "*result*" of binary search| Displaying Result Of Binary Search]]

---

- [[Queue ADT - 1D Array ( Mine )#Queue Program Code Example| Example]]
	- [[Queue ADT - 1D Array ( Mine )#Full Queue Code ( Template )| Template]]

---

My Links

- [[Queue ADT - 1D Array ( Mine )#Socials| Links to Social]]

---

# What is a Queue?

It forms part of the [[Python Data View#Abstract Data Types | abstract data types ]] family. It is a collection of elements with **2** main *operations* and **2** *pointers*

Nevertheless, this is not like [[Stack ADT - 1D Array ( Mine )]]. Because we do not *move* data the same way as we do in **Stack**. The reason is that **Queue** is a "*FIFO*" data structure. Now you might think to yourself! What the heck is *FIFO*? Well Sir, you have come the right place to know. It stands for:

$$First \ In \ First \ Out$$

## Operations of Queue ADT

1. **Enqueue** Operation
	- To **add** elements to the queue / array
2. **Dequeue** Operation
- To **remove** elements from the queue / array

Think of the **Queue Data Structure** as if you standing in a line waiting for an icecream.

### Enqueue Operation

So, think of the *icecream van* as an array! You would wait for you turn and you would stand in a line ( *nowadays we are all bad boys, there is no line and respect anymore... except for Japan!* ).

Now when its your turn; you will **enter** ( *enqueue into* ) the *array*.

This is what the **enqueue** operation basically is. But remember we need to "*remember*" that there are still people behind.

### Dequeue Operation

Now that you have got your desired icecream, you need to **exit** ( *dequeue from* ) the *array*; so that the next person could **enter** ( *enqueue* ).

Thus this is why we called it the **FIFO** structure $\rightarrow$ **FIRST IN FIRST OUT**

## Pointers

This is why I said:

>We need to "remember" that there are still people behind

This is because compared to [[Stack ADT - 1D Array ( Mine )#Pointer| stack]], **Queue** has **2** pointer.

- One will point to the front of the array
	- This pointer will move after **adding** and **removing** data
- Another one will point the the back of the array
	- This one will always points the the **last item**

---

# Photo

This is an example photo of how **Queue ADT** works

![[Queue ADT  Explanation.png| 625]]

---

# Queue Program Code

For the moment, I will only write the [[Functions and Procedures - Python|functions]] that makes up the full *queue data structure*. Thus, it will be easier for you to learn and understand the code as they are separate from each other.

## Functions

## Initialising our Queue

For this, we need to make an array and **2** global variables

```python

# Queue Program Code

# Array with identifier name "queue"
# DECLARE queue: ARRAY[] OF INTEGER
queue = []

# Global variable "front" which will keep track of the last item inserted
# DECLARE front: OF INTEGER
global front

# Global variable "rear" which will keep track of the newest item
# DECLARE rear: OF INTEGER
global rear

```

## Displaying Array

This is a function that can be called to display the array

```python

# Queue Program Code

def display_array():

    # If array "queue" is empty
    if not queue:

        # If array is EMPTY; then pointer "front" will be "0"
        front = -1

        # If array is EMPTY ( again ); then pointer "rear" will be "-1"
        rear = -1

        # Output appropriate message if array is empty
        print()
        print("ARRAY IS EMPTY!")
        print()

        # Displays the "front" and "rear" pointer
        print("Front: " + str(front))
        print("Rear: " + str(rear))
        print()

    # If NOT empty, prints values line by line
    else:

        print()

        # Prints elements line by line
        for x in queue:

            print(x)

        front = len(queue) -1
        rear = 0

        print()
        print("Front: " + str(front))
        print("Rear: " + str(rear))
        print()

```

>[!info]
>In this case the lower bound of our array is "1"
>To be **honest** with you, I do not really know and I need to ask someone qualified to baby me and show me why.

## Inserting Values

This function will allow the user to enter value in array

```python

# Queue Program Code

def insert_values_insert():

    # Exception Handling
    try:

        # Variable "front" takes length of array
        front = len(queue) -1

        # Variable "rear" will be set to "-1"
        rear = -1

        # Ask the user to enter size of array
        queue_size = int(input("Please Enter Size Of Array: "))

        print()

        # Entering Data into array
        for i in range(queue_size):

            # Ask the user to enter a value
            user_input = int(input("Please Enter A Value: "))

            # Inserts data into array
            # Function insert is used like this: "insert("address", "data")"
            queue.insert(0, user_input)

            # Increments "front" by one
            front += 1

        # Rear pointer "rear" become "0"
        rear = 0

    # If user inputs any other character other than Integer values
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

```

>[!tip] Another Way To Insert Values
>The second method of adding value to array is the use:
>```python
>.append()
>```
>But this one will require a different *pop* function

## Pop Function

This is self-explanatory, though in this case it will be used to remove the **first** item *added*

```python

# Queue Program Code

def remove_pop_values():

    # Removes the first value added to array ( "last" value )
    queue.pop()

    print()

```

>[!tip] Another Way to Pop a Value
>The second method of adding value to array is the use:
>```python
>pop(0)
>```
>But this one need to be used with *.append()* function when inserting values into array.

>[!info]
>```python
>pop()
>```
>- It can also remove an element at any address by passing the address inside the function
>- But in our use case, we only need to remove the first item, so no need to pass any values inside function.

## Delete Specific Element

This function will allow a user to:

- Enter a value
- If the value if found
	- The function will remove the value
- Else
	- The function will output an appropriate message

### With ONLY **FOR Loop**

```python

# Queue Program Code

def remove_user_values():

    # Exception Handling
    try:

        # If array "queue" is empty
        if not queue:

            # Initialising Our Pointers

            # Variable "rear" will be equal to "-1"
            rear = -1

            # Variable "front" will be equal to "0"
            front = 0

            # Outputs appropriate message
            print()
            print("Array Is Already EMPTY")
            print("NOTHING TO REMOVE!")
            print()

            # Displaying Pointers
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

        # If array "queue" is NOT empty
        else:

            # Front pointer "front" takes the length of array
            front = len(queue)

            # Rear pointer "rear" becomes "0"
            rear = 0

            # Variable "array_length" will hold the length of array "queue"
            array_length = len(queue)

            # Variable "Found" will keep track if the value to remove has been found
            Found = False

            # Ask the user to enter a value to remove
            user_remove = int(input("Please Enter A Value To Remove: "))

            # Steps through the array
            for i in range(array_length):

                # If value to remove has been found
                if queue[i] == user_remove:

                    # Removes "user_remove"
                    queue.remove(user_remove)
                    Found = True
                    print(str(user_remove) + " has been removed!")
                    
                    # Variable "front" decreases by 1
                    front -= 1

                    # Escapes for loop ( found )
                    break

            # If "user_remove" has not been found
            if Found == False:

                # Output appropriate message
                print()
                print(str(user_remove) + " has NOT been found!")
                print()

    # If user inputs any other "character" other than Integer values
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

```

### With **WHILE Loop**

```python

# Queue Program Code

def remove_value_while():

    # Exception Handling
    try:

        # If array "queue" is empty
        if not queue:

            # Initialising Our Pointers

            # Variable "rear" will be equal to "-1"
            rear = -1

            # Variable "front" will be equal to "0"
            front = 0

            # Outputs appropriate message
            print()
            print("Array Is Already EMPTY")
            print("NOTHING TO REMOVE!")
            print()

            # Displaying Pointers
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

        # If array "queue" is NOT empty
        else:

            # Front pointer "front" takes the length of array
            front = len(queue)

            # Rear pointer "rear" becomes "0"
            rear = 0

            # Variable "array_length" will hold the length of array "queue"
            array_length = len(queue)

            # Variable "Found" will keep track if the value to remove has been found
            Found = False

            # Ask the user to enter a value to remove
            user_remove = int(input("Please Enter A Value To Remove: "))

            # Condition to enter array "queue"
            while not Found:

                # Steps through array
                for i in range(array_length):

                    # If value has been found
                    if queue[i] == user_remove:

                        # Function removes value
                        queue.remove(user_remove)
                        Found = True

                        # Decrease pointer "front" by 1
                        front -= 1

                        # Escapes for loop ( found )
                        break

                # Escapes while loop ( NOT found )
                break

            # Displays pointers "front" and "rear"
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

            # When value had NOT been found
            if Found == False:

                # Outputs appropriate message
                print()
                print(" has Not been found!")
                print()

    # If user inputs any other character other than integer values
    except ValueError:

        print()
        print("Please Enter Integer Values Only")
        print()

```

>[!warning]
>This is not really advised, because I often have problem with
>Like the code is **good**, but for simplicity, the **for** loop does *everything* we need to
>Thus, **better to use the for loop only** and also, number of lines reduces and it is easier to learn

## Bubble Sort

This function will allow us to sort the array in ascending order; why *ascending order you make ask?*; This is because **binary search** requires the array to be sorted ( **ascending order** ).

```python

# Queue Program Code

def bubble_sort():

    # Variable "array_length" will hold the length of array
    array_length = len(queue)

    # Variable "swaps" will cound how many times, values have been swapped
    swaps = 0

    # Variable "update" will become "True" if array has been sorted
    update = True

    # Sorting part of algorithm ( bubble sort optimised )
    while update == True and array_length > 1:

        # Variable "update" becomes "False" as it need to become "updated" after swap
        update = False

        for x in range(0, array_length -1):
            for y in range(0, array_length - 1):

                # Ascending Order
                # This is because "Binary Search" will need the array in ascending order
                if queue[y] > queue[y + 1]:

                    # Swapping Part
                    temp = queue[y]
                    queue[y] = queue[y + 1]
                    queue[y + 1] = temp
                    # "swaps" increments by 1

                    swaps += 1
                    # "update" becomes "True" as value has been swapped
                    update = True

```

## Insertion Sort

Another method we could have use is ( *drum-roll* ) **insertion sort**. To be honest, just use [[Queue ADT - 1D Array ( Mine )#Bubble Sort| bubble sort]], it is much better to use **bubble sort** as it is more efficient for large data set.

Nevertheless, here is the code.

```python

# Queue Program Code

def insertion_sort():

    # Variable "array_length" will hold the length of array
    array_length = len(queue)

    # Sorting part of algorithms
    for i in range(1, array_length):

        # Variable "values" will hold the values at address "i"
        values = queue[i]

        # Variable "j" will hold the value to the left of "values" or "i"
        j = i - 1

        # Condition to enter "while" loop
        # The part "queue[j] > values" ( ascending order )
        # It checks if for example: index 0's value is > than index 1's value
        # If "yes" then it swaps
        while j >= 0 and queue[j] > values:

            # Swapping Part
            queue[j + 1] = queue[j]

            # Decreases "j" by one
            j -= 1

        # If array already sorted
        queue[j + 1] = values

```

## Linear Search

This function is a nice and **simple** one; like a good old friend that will help you to find your way.

What else can I say, its just a [[Python Data View#Searching Algorithms| search algorithm]]

```python

# Queue Program Code

def linear_search():

    # Exception Handling
    try:

        # Variable "array_length" will hold the length of array
        array_length = len(queue)

        # Ask the user for a value to search
        search_value = int(input("Please Enter A Value To Search: "))

        # Searching Algorithm
        # Steps through array "queue"
        for i in range(0, array_length):

            # If value to be searched has been found
            if queue[i] == search_value:

                # Returns the address of "search_value"
                return i

        # Else if NOT found
        return - 1

    # If user enter any other character except Integer values
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

```

### Displaying the "*result*" of Linear Search

```python

# Queue Program Code

result_linear = linear_search()

# If search value has been found
if result_linear != -1:

    # Output appropriate message
    print("Value has been found at address: " + str(result_linear))

# If search value has NOT been found
else:

    # Outputs appropriate message
    print("Your value has not been found")

```

## Binary Search

This is another much better way of searching for an element/item. 
This is because it cuts the array every time it does not find the "*value*".

```python

# Queue Program Code

def binary_search(queue, search_value):

    return binary_search_calc(queue, 0 , len(queue) -1, search_value)

def binary_search_calc(queue, lower, upper, search_value):

    # Condition to peform binary search
    while lower <= upper:

        # Calculates the mid-point of array
        mid = (lower + upper) // 2

        # If "search_value" is at midpoint; we return the address
        if queue[mid] == search_value:

            return mid

        # If value at mid-point is < than search value; we cut bottom part of array
        elif queue[mid] < search_value:

            lower = mid + 1

        else:

            # If value at mid-point is > than search value; then we cut upper part of array
            upper = mid - 1

    # If value has NOT been found
    return - 1

```

### Displaying the "*result*" of Binary Search

```python

# Queue Program Code

# Asking user to enter a value to search
# Exception Handling
try:

    search_value = int(input("Please Enter A Value To Search: "))

except ValueError:

    print()
    print("Please Enter Integer Values Only!")
    print()

result_binary = binary_search(queue, search_value)

if result_binary != -1:

    # Output appropriate message

    print("Value has been found at address: " + str(result_binary))

# If search value has NOT been found
else:

    # Outputs appropriate message
    print("Your value has not been found")

```

---

# Queue Program Code Example

## Full Queue Code ( Template )

```python

# Queue Program Code

# Queue Program Code

# Array with identifier name "queue"
queue = []

# Global variable "front" which will keep track of the last item inserted
global front

# Global variable "rear" which will keep track of the newest item added
global rear

def display_array():

    # If array "queue" is empty
    if not queue:

        # If array is EMPTY; then pointer "front" will be "0"
        front = 0

        # If array is EMPTY ( again ); then pointer "rear" will be "-1"
        rear = - 1

        # Output appropriate message if array is empty
        print()
        print("ARRAY IS EMPTY!")
        print()

        # Displays the "front" and "rear" pointer
        print("Front: " + str(front))
        print("Rear: " + str(rear))
        print()

    # If NOT empty, prints values line by line
    else:

        print()

        # Prints elements line by line
        for x in queue:

            print(x)

        front = len(queue)
        rear = 0

        print()
        print("Front: " + str(front))
        print("Rear: " + str(rear))
        print()

def insert_values_insert():

    # Exception Handling
    try:

        # Variable "front" takes length of array
        front = len(queue)

        # Variable "rear" will be set to "-1"
        rear = -1

        # Ask the user to enter size of array
        queue_size = int(input("Please Enter Size Of Array: "))

        print()

        # Entering Data into array
        for i in range(queue_size):

            # Ask the user to enter a value
            user_input = int(input("Please Enter A Value: "))

            # Inserts data into array
            # Function insert is used like this: "insert("address", "data")"
            queue.insert(0, user_input)

            # Increments "front" by one
            front += 1

        # Rear pointer "rear" become "0"
        rear = 0

    # If user inputs any other character other than Integer values
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

def remove_pop_values():

    # Removes the first value added to array ( "last" value )
    queue.pop()

    print()

def remove_user_values():

    # Exception Handling
    try:

        # If array "queue" is empty
        if not queue:

            # Initialising Our Pointers
            # Variable "rear" will be equal to "-1"
            rear = -1

            # Variable "front" will be equal to "0"
            front = 0

            # Outputs appropriate message
            print()
            print("Array Is Already EMPTY")
            print("NOTHING TO REMOVE!")
            print()

            # Displaying Pointers
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

        # If array "queue" is NOT empty
        else:

            # Front pointer "front" takes the length of array
            front = len(queue)

            # Rear pointer "rear" becomes "0"
            rear = 0

            # Variable "array_length" will hold the length of array "queue"
            array_length = len(queue)

            # Variable "Found" will keep track if the value to remove has been found
            Found = False

            # Ask the user to enter a value to remove
            user_remove = int(input("Please Enter A Value To Remove: "))

            # Steps through the array
            for i in range(array_length):

                # If value to remove has been found
                if queue[i] == user_remove:

                    # Removes "user_remove"
                    queue.remove(user_remove)

                    # Variable "Found" becomes "True"
                    Found = True

                    # Variable "front" decreases by 1
                    front -= 1

                    # Escapes "for" loop
                    break

            # If "user_remove" has not been found
            if Found == False:

                # Output appropriate message
                print()
                print(str(user_remove) + " has NOT been found!")
                print()

    # If user inputs any other "character" other than Integer values
    except ValueError:

        # Outputs appropriate message

        print()
        print("Please Enter Integer Values Only!")
        print()

def remove_value_while():

    # Exception Handling
    try:

        # If array "queue" is empty
        if not queue:

            # Initialising Our Pointers
            # Variable "rear" will be equal to "-1"
            rear = -1

            # Variable "front" will be equal to "0"
            front = 0

            # Outputs appropriate message
            print()
            print("Array Is Already EMPTY")
            print("NOTHING TO REMOVE!")
            print()

            # Displaying Pointers
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

        # If array "queue" is NOT empty
        else:

            # Front pointer "front" takes the length of array
            front = len(queue)

            # Rear pointer "rear" becomes "0"
            rear = 0

            # Variable "array_length" will hold the length of array "queue"
            array_length = len(queue)

            # Variable "Found" will keep track if the value to remove has been found
            Found = False

            # Ask the user to enter a value to remove
            user_remove = int(input("Please Enter A Value To Remove: "))

            # Condition to enter array "queue"
            while not Found:

                # Steps through array
                for i in range(array_length):

                    # If value has been found
                    if queue[i] == user_remove:

                        # Function removes value
                        queue.remove(user_remove)
                        Found = True

                        # Decrease pointer "front" by 1
                        front -= 1

                        # Escapes for loop ( found )
                        break

                # Escapes while loop ( NOT found )
                break

            # Displays pointers "front" and "rear"
            print()
            print("Front: " + str(front))
            print("Rear: " + str(rear))
            print()

            # When value had NOT been found
            if Found == False:

                # Outputs appropriate message
                print()
                print(" has Not been found!")
                print()

    # If user inputs any other character other than integer values
    except ValueError:

        print()
        print("Please Enter Integer Values Only")
        print()

def bubble_sort():

    # Variable "array_length" will hold the length of array
    array_length = len(queue)

    # Variable "swaps" will cound how many times, values have been swapped
    swaps = 0

    # Variable "update" will become "True" if array has been sorted
    update = True

    # Sorting part of algorithm ( bubble sort optimised )
    while update == True and array_length > 1:

        # Variable "update" becomes "False" as it need to become "updated" after swap
        update = False

        for x in range(0, array_length -1):
            for y in range(0, array_length - 1):

                # Ascending Order
                # This is because "Binary Search" will need the array in ascending order
                if queue[y] > queue[y + 1]:

                    # Swapping Part
                    temp = queue[y]
                    queue[y] = queue[y + 1]
                    queue[y + 1] = temp

                    # "swaps" increments by 1
                    swaps += 1

                    # "update" becomes "True" as value has been swapped
                    update = True

  

def insertion_sort():

    # Variable "array_length" will hold the length of array
    array_length = len(queue)

    # Sorting part of algorithms
    for i in range(1, array_length):

        # Variable "values" will hold the values at address "i"
        values = queue[i]

        # Variable "j" will hold the value to the left of "values" or "i"
        j = i - 1

        # Condition to enter "while" loop
        # The part "queue[j] > values" ( ascending order )
        # It checks if for example: index 0's value is > than index 1's value
        # If "yes" then it swaps
        while j >= 0 and queue[j] > values:

            # Swapping Part
            queue[j + 1] = queue[j]

            # Decreases "j" by one
            j -= 1

        # If array already sorted
        queue[j + 1] = values

def linear_search():

    # Exception Handling
    try:

        # Variable "array_length" will hold the length of array
        array_length = len(queue)

        # Ask the user for a value to search
        search_value = int(input("Please Enter A Value To Search: "))

        # Searching Algorithm
        # Steps through array "queue"
        for i in range(0, array_length):

            # If value to be searched has been found
            if queue[i] == search_value:

                # Returns the address of "search_value"
                return i

        # Else if NOT found
        return - 1

    # If user enter any other character except Integer values
    except ValueError:

        # Outputs appropriate message
        print()
        print("Please Enter Integer Values Only!")
        print()

def binary_search(queue, search_value):

    return binary_search_calc(queue, 0 , len(queue) -1, search_value)

def binary_search_calc(queue, lower, upper, search_value):

    # Condition to peform binary search
    while lower <= upper:

        # Calculates the mid-point of array
        mid = (lower + upper) // 2

        # If "search_value" is at midpoint; we return the address
        if queue[mid] == search_value:

            return mid

        # If value at mid-point is < than search value; we cut bottom part of array
        elif queue[mid] < search_value:

            lower = mid + 1

        else:

            # If value at mid-point is > than search value; then we cut upper part of array
            upper = mid - 1

    # If value has NOT been found
    return - 1

  

# Calling Function
print()
print("Displaying Array ( INITIALLY )")

display_array()

print()
print("Inserting Data Into Array")
print()

insert_values_insert()

display_array()

print()
print("Removing The First Value Added To Queue")

remove_pop_values()

print()
print("Displaying Array After Removing First Value ( Added )")
print()

display_array()

print()
print("User Removes Value From Array")
print()

remove_user_values()

print("Displaying Array After User Removes A Value")
print()

display_array()

bubble_sort()

#insertion_sort()

print("Displaying Array After Bubble Sort")
print()

display_array()

print("Linear Search")
print()

result_linear = linear_search()

# If search value has been found
if result_linear != -1:

    # Output appropriate message
    print("Value has been found at address: " + str(result_linear))

# If search value has NOT been found
else:

    # Outputs appropriate message
    print("Your value has not been found")

print()
print("Binary Search")
print()

# Asking user to enter a value to search

# Exception Handling
try:

    search_value = int(input("Please Enter A Value To Search: "))

except ValueError:

    print()
    print("Please Enter Integer Values Only!")
    print()

result_binary = binary_search(queue, search_value)

if result_binary != -1:

    # Output appropriate message
    print("Value has been found at address: " + str(result_binary))

# If search value has NOT been found
else:

    # Outputs appropriate message
    print("Your value has not been found")

print()

```

>[!info]
>The function "**insertion_sort()**" is not used in this code, though we could remove "*#*" to be able to use it.
---

# Socials

- [**Instagram:**](https://www.instagram.com/s.sunhaloo/)
- [**YouTube:**](https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg)

---

S.Sunhaloo
Thank You!