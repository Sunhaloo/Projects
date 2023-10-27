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

# calling function
display()

enqueue(4)
enqueue(4)
enqueue(4)
enqueue(4)
enqueue(4)
enqueue(4)

display()

dequeue()
dequeue()
dequeue()
dequeue()

display()

specific_delete(4)

display()

# This is not the completed version
# But I have managed to make these necessary function works:)
