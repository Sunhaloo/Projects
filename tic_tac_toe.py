# make the board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

current_play = "X"
game_running = True
winner = None


# create function to display board
def display_board():
    print("\nBoard\n")
    print("-" * 13)
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-" * 13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-" * 13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-" * 13)


# create function to accept user_input
def user_input():
    global current_play

    # ask the user to input number / where to place his 'pion'
    player_input = int(input("Please Enter Your Number ( 1 to 9 ): "))

    if player_input >= 1 and player_input <= 9:
        # check if board does not have anohter player's 'pion'
        if board[player_input - 1] == "-":
            board[player_input - 1] = current_play
        # if board contains another player's 'pion'
        else:
            print("\nSpace is Already Occuppied")
    else:
        print("\nYou have not entered the right number\n")
        # recursion / recursive
        user_input()


# create function to change the player's 'pion'
def change_turn():
    global current_play
    if current_play == "X":
        current_play = "O"
    elif current_play == "O":
        current_play = "X"


# create function to check if win in horizontal direction
def horizontal_win():
    global current_play
    global game_running
    global winner
    # need to add this because then '-' all the way would be win
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        print(f"\nWinner is {winner}")
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        print(f"\nWinner is {winner}")
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        print(f"\nWinner is {winner}")

    # end the game
    if winner != None:
        game_running = False


# create function to check if win in horizontal direction
def vertical_win():
    global current_play
    global game_running
    global winner
    # need to add this because then '-' all the way would be win
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        print(f"\nWinner is {winner}")
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        print(f"\nWinner is {winner}")
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        print(f"\nWinner is {winner}")

    # end the game
    if winner != None:
        game_running = False


# create a function to check win in diagonals
def diags_win():
    # calling global variables to function 'diags_win'
    global current_play
    global game_running
    global winner

    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = current_play
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = current_play

    if winner != None:
        game_running = False


# create a function to check for ties
def ties():
    if "-" not in board:
        display_board()
        print("TIE")
        game_running = False


# create main game function
def game():
    global game_running
    while game_running == True:
        # call functions
        display_board()
        user_input()
        horizontal_win()
        vertical_win()
        change_turn()


# calling main game function
game()
