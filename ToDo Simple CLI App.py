# Simple ToDo CLI Application in Python
# Author: S.Sunhaloo
# Date: 30/03/2024

# DECLARE ARRAY tasks: STRING
# Array which will hold the tasks
tasks = []


# FUNCTION text
# Will display main message / welcome screen to user
def text():
    # Display Welcome Screen and Options
    print()
    print("---------")
    print("TODO App")
    print("---------")
    print()
    print("To Choose Option ---> Enter Its Number")
    print()
    print("Display Task(s): 1")
    print("Add Task(s): 2")
    print("Delete Task(s): 3")
    print("Modify Task: 4")
    print()


# FUNCTION display_tasks
# Will be reponsible for displaying tasks
def display_tasks():
    
    print()

    # If there is NOTHING in array `tasks`
    if not tasks:
        print()
        print("You have no tasks left!!!")
        print()

    else:
        # Display Array `tasks`
        for index, x in enumerate(tasks):
            print(f"Task #{index}: {x}")


# FUNCTION add_tasks
# Will allow the user to enter task(s) into array
def add_tasks():
    
    # Exception Handling
    try:

        print()
        # Ask the user how many tasks to add
        num_of_tasks = int(input("Please Enter Number of Task to Add: "))

        print()

        # Iterate
        for i in range(num_of_tasks):

            # DECLARE user_task: STRING
            # Ask the user to enter task
            user_task = input(f"Task #{i}: ")

            # Add / Append task to array `tasks`
            tasks.append(user_task)

    except ValueError:

        print()
        print("Please Enter The Required Information")
        print()


# FUNCTION delete_tasks
# Will allow user to delete task(s)
def delete_tasks():

    # Exception Handling
    try:

        # DECLARE num_of_delete
        # Ask the user to enter the number of tasks to delete
        num_of_delete = int(input("Please Enter Amount of Task to Delete: "))

        print()

        # Iterate
        for y in range(num_of_delete):

            # Displaying Array
            # Else we could have an error in terms of size of array
            # The simplest solution to this is to output the array to user each time
            # Call Function `display_tasks`
            display_tasks()
            
            print()

            # Ask the user to enter index to delete
            delete_index = int(input("Please Enter Index ( # ) of Task: "))

            # Condition to satisfy to continue
            if delete_index >= 0 and delete_index < len(tasks):

                # Forgot that this is NOT C!!! ( Look At Comments Below )
                tasks.pop(delete_index)

                # Output what has been deleted
                print(f"--->Task #{delete_index} Has Been Deleted<---")

                # No Need to Iterate to Find Index
                # Iterate through array `tasks` to find index
                    # for x in range(array_index):
                # If we find the index
                        # if x == delete_index:
                        # Remove tasks
                        # Method 1
                            # del tasks[delete_index]
                        # Method 2
                            # tasks.pop(delete_index)

            else:

                # The index entered does not exists
                print(f"---> Invalid Number Entered / #{delete_index} Has Not Been Found <---")
                print()

    except ValueError:

        print()
        print("Please Enter Required Information")
        print()


# FUNCTION modify
# Will allow user to modify a task ( value at that index ) in array `tasks`
def modify():

    # Call Function `display_task` to display tasks
    display_tasks()

    print()

    # Exception Handling
    try:

        # DECLARE modify_index: INTEGER
        # User will enter the index; where user wants to change value
        modify_index = int(input("Please Enter Index to Modify: "))

        # DECLARE index_found: BOOLEAN
        # Checks if that the index is found
        index_found = False

        print()

        # Iterate
        for z in range(len(tasks)):

            if z == modify_index:

                # Ask the user to enter new value
                new_value = input("Please Enter New Value: ")

                # Change the value in array at that location
                tasks[z] = new_value

                # Because index is found; `index_found` becomes `True`
                index_found = True

                # Escape `for` Loop
                break

        # If index is NOT found
        if not index_found:

            print()
            # Outputs appropriate message
            print(f"---> Invalid Number Entered / #{modify_index} Has Not Been Found <---")
            print()

    except ValueError:

        print()
        print("Please Enter Required Information")
        print()


# FUNCTION main
# Will be the one to "hold" everything
def main():

    # Call Function `text`
    text()

    # Exception Handling
    try:

        # DECLARE user_choice: INTEGER
        # Ask the user to enter a choice
        user_choice = int(input("Please Enter Your Choice ( Enter Number ): "))

        # Switch Case
        match user_choice:

            case 1:
                # Call Function `display_tasks`
                display_tasks()
            case 2:
                # Call Function `add_tasks`
                add_tasks()
            case 3:
                # Call Function `delete_tasks`
                delete_tasks()
            case 4:
                # Call Function `modify`
                modify()

        print()

        # DECLARE see_task: STRING
        # Ask the user if he wants to review task list again
        see_task = input("Do You Want to See Your Tasks Again [Y/n]? ")

        # Condition
        if see_task == "Y":

            # Call Function `display_tasks` again
            display_tasks()

            print()

            # Ask the user if wants to exits program
            exits = input("Do You Want To Exit Program [Y/n]?: ")

            # Condition
            if exits == "Y":

                # Calls the `exit()` Function
                exit()

            else:

                # Calls `main` Function again
                main()

        else:

            # DECLARE exits: STRING
            # Ask the user if he wants to exits program
            exits = input("Do You Want To Exit Program [Y/n]?: ")

            # Condition
            if exits == "Y":

                # Calls the `exit()` Function
                exit()

            else:

                # Calls `main` Function again
                main()

    except ValueError:

        print()
        print("Please Enter Required Information")
        print()

    print()


# Calling `main` Function to Run Program
main()
