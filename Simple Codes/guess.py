import random

print()
print("RANDOM NUMBER GUESSER GAME")
print()

# make a random number from 1 to 100
rand_num = random.randint(1, 100)

# global variables holding the names of players
global Player1
global Player2

print("Please Enter Both Player's Names")
print()

# ask the players to enter their names
Player1 = input("Please Enter Player 1's Name: ")
Player2 = input("Please Enter Player 2's Name: ")

# make a function to ask the players to enter a number

def ask():
    # using global function ( from main program )
    global Player1
    global Player2

    # exception handling
    try:

        print()
        print("For Both Players; Please Enter A Number Between 1 and 100")
        print()

        global player1_num
        global player2_num

        # "getting" the numbers
        player1_num = int(input(f"{Player1}'s Number: "))
        player2_num = int(input(f"{Player2}'s Number: "))
        print()

    except ValueError:

        print()
        print("Please Enter Integer Numbers Only!")
        print()

# make a function to guess to numbers
def guess():

    # using our global variables
    global Player1
    global Player2
    global player1_num
    global player2_num

    # calculate the difference between random and number guessed by players
    player1Diff = abs(rand_num - player1_num)
    player2Diff = abs(rand_num - player2_num)

    # winning conditions
    
    # we have to check for "draw" FIRST
    if player1_num == rand_num and player2_num == rand_num:

        print()
        print("Draw")
        print()

    elif player1_num == rand_num:

        print()
        print(f"Winner is {Player1}!")
        print()

    elif player1_num == rand_num:

        print()
        print(f"Winner is {Player2}!")
        print()

    elif player1Diff > player2Diff:

        print()
        print(f"Winner is {Player2}!")
        print()

    else:

        print()
        print(f"Winner is {Player1}!")
        print()

# main function
def main():

    # make a boolean value to check if players will still play
    play = True

    # condition to "play"
    while play:

        # call our functions to play the game
        ask()
        guess()

        # exception handling
        try:

            # ask the user if wants to play again
            play_again = str(input("Would you like to play again(y/n): "))

            # player does not want to play
            if play_again == "n":

                # program will not enter "while" loop
                play = False

            else:

                # program will continue to play
                play = True

            print()

        except TypeError:

            print()
            print("Please enter 'y' or 'n' only!")
            print()

            print("Exiting Program")

            # does not enter "while" loop
            play = False

# calling only one "main" function
main()
