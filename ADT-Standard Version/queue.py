# Queue Program Code

global front
global rear
global queue_length

queue_length = 5

queue = []

def display():

    if not queue:

        front = -1
        rear = -1

        print()
        print("Array is EMPTY")
        print()

        print(f"Front: {front}")
        print(f"Rear: {rear}")
        print()

    else:

        for x in queue:

            print(x)

        front = len(queue) -1
        rear = 0

        print()
        print(f"Front: {front}")
        print(f"Rear: {rear}")
        print()

def enqueue(item):

    front = len(queue) -1
    queue_length = 5

    if front == queue_length -1:

        print()
        print("Array is already FULL")
        print()

    elif front < queue_length -1:

        front += 1

        queue.insert(0, item)

def dequeue():

    front = len(queue) -1

    global queue_length

    if queue_length == 0:

        rear = -1

        print()
        print("Array is already EMPTY")
        print()

    else:

        queue.pop()
        front -= 1
        queue_length -= 1

def specific_delete(item):

    global front
    global rear
    global queue_length

    array_length = len(queue)

    front = len(queue) -1

    if queue_length == 0:

        print()
        print("Array is already EMPTY")
        print()

    else:

        found = False

        for x in range(array_length):

            if queue[x] == item:

                queue.remove(queue[x])
                print(f"{item} has been removed")

                found = True

                front -= 1

                queue_length -= 1

                break

        if not found:

            print()
            print(f"{item} has NOT been found")
            print()

def bubble_sort():

    update = True

    swap = 0

    array_length = len(queue)

    while update == True and array_length > 0:

        update = False

        for x in range(0, array_length -1):

            for y in range(0, array_length -1):

                # sorting in ascending order
                if queue[y] > queue[y +1]:

                    temp = queue[y]
                    queue[y] = queue[y + 1]
                    queue[y + 1] = temp

                    update = True

                    swap += 1

def insertion_sort():

    array_length = len(queue)

    for x in range(1, array_length):

        values = queue[x]

        y = x -1

        while y >= 0 and queue[y] > values:

            queue[y + 1] = queue[y]

            y -= 1

        queue[y + 1] = values

def linear_search(item):

    array_length = len(queue)

    for x in range(0, array_length):

        if queue[x] == item:

            return x
    
    return -1

def binary_search(item):

    return binary_search_calc(0, len(queue) -1 , queue, item)

def binary_search_calc(lower, upper, queue, item):

    while lower <= upper:

        mid = (lower + upper) // 2

        if queue[mid] == item:

            return mid
        
        elif queue[mid] < item:

            lower = mid +1

        else:

            upper = mid -1

# calling function 
display() 
enqueue(19)
enqueue(8)
enqueue(4)
enqueue(24)
enqueue(40)
enqueue(4)

display()

dequeue()
dequeue()
specific_delete(4)

display()

#bubble_sort()
insertion_sort()

display()

result_linear = linear_search(24)

def display_linear(result):

    if result != -1:

        print(f"Found at {result}")

    else:
        
        print("Has not has not been found")


display_linear(result_linear)

result_binary = binary_search(40)

def display_binary(result):

    if result != -1:

        print(f"Found at {result}")

    else:

        print("Has not been found")

display_binary(result_binary)
