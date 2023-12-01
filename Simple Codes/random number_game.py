import random

print()

# make a random number generator
random_num = random.randint(1, 100)

# make function to input users name
def ask_names():

    # global variables
    global name1
    global name2

    name1 = ""
    name2 = ""

    try:

        # input names
        while name1 == "":

            print()
            print("Enter Player Name")
            print()

            name1 = input("Player 1 Name: ")

            print()

            if name1 != "":

                change_name1 = input("Would You Like To Change Your Name(y/n): ")

                if change_name1 == "y":

                    # Why is this line causing problems
                    # while name1 == "":

                        print()
                        print("Enter Player 1's Name")
                        print()

                        name1 = input("Player 1 Name: ")

                elif change_name1 == "n":

                    continue

        while name2 == "":

            print()
            print("Enter Player Name")
            print()

            name2 = input("Player 2 Name: ")

            print()

            if name2 != "":
             
                change_name2 = input("Would You Like To Change The Name(y/n): ")

                if change_name2 == "y":

                    # Why is this line causing problems
                    # while name2 == "":

                    print()
                    print("Enter Player 2's Name")
                    print()

                    name2 = input("Player 2 Name: ")

                elif change_name2 == "n":

                    continue

            print()

            while name2 == "":

                print()
                print("Enter Player 2's Name'")
                print()

                name2 = input("Player 2 Name: ")

        print()
        print("Displaying Players Names")
        print()

        print("Player 1 | Player 2")
        print("---------------------")
        print(f"{name1}  |  {name2}")
        print()

    except ValueError:

        print()
        print("Please Enter Required Values Only!")
        print()

# function to ask users to enter their number
def ask_numbers():

    # creating global variables
    global player_num1
    global player_num2
    # using global variable
    global name1
    global name2

    try:

        # ask the players to enter a number between 1 and 100
        while True:

            print()
            print("Please Enter A Number Between 1 and 100")
            print()

            player_num1 = int(input(f"{name1} Please Enter A Number: "))

            if 1 <= player_num1 <= 100:

                print()
                print("Number is in Range!")
                print()

                break

            else:

                print()
                print("Number is not in Range")
                print()

        while True:

            print()
            print("Please Enter A Number Between 1 and 100")
            print()

            player_num2 = int(input(f"{name2} Please Enter A Number: "))

            if 1 <= player_num2 <= 100:

                print()
                print("Number is in Range!")
                print()

                break

            else:

                print()
                print("Number is not in Range")
                print()

        print()
        print("Displaying Numbers")
        print()

        print(f"{name1}'s Number | {name2}'s Number")
        print("-------------------------------")
        print(f"       {player_num1}    |       {player_num2}")
        print()


    except ValueError:

        print()
        print("Please Enter Integer Numbers Only")
        print()

# make a function to guess the numbers
def guess_numbers():

    # using global variables
    global name1
    global name2
    global player_num1
    global player_num2

    # calculating difference
    player_diff_num1 = abs(random_num - player_num1)
    player_diff_num2 = abs(random_num - player_num2)

    # winning conditions
    
    # need to check if draw FIRST
    if player_num1 == random_num and player_num2 == random_num:

        print()
        print("Draw")
        print()

    elif player_num1 == random_num:

        print()
        print(f"{name1} Wins")
        print()

    elif player_num2 == random_num:

        print()
        print(f"{name2} Wins")
        print()

    elif player_diff_num1 > player_diff_num2:

        print()
        print(f"Winner is {name2}!")
        print()

    else:

        print()
        print(f"Winner is {name1}!")
        print()


# main function
def main():

    print()
    print("RANDOM NUMBER GUESSER GAME")
    print()

    game_running = True

    while game_running:

        # calling functions inside "main" functions
        ask_names()
        ask_numbers()
        guess_numbers()

        try:

            # ask user to play again
            play_again = input("Would You Like To Play Again(y/n)")
            print()

            if play_again == "n":

                game_running = False

            else:

                game_running = True

        except TypeError:

            print()
            print("Please Enter 'y' or 'n' Only!")
            print()

            print("Exiting Program")
            print()

            game_running = False



# calling function
main()
