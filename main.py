
player = 0
player1 = ""
player2 = ""
player_choice = ""
playing = True
repeat = True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_board = ""

numbered_board = " 1 | 2 | 3 \n---|---|---\n 4 | 5 | 6 \n---|---|---\n 7 | 8 | 9 "

number_dictionary = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}


def game_board():
    global number_dictionary
    global current_board
    # Executes replacement to update current board
    number_dictionary = replacement(player, player_choice)
    current_board = f" {number_dictionary[1]} | {number_dictionary[2]} | {number_dictionary[3]} \n" \
                    f"---|---|---\n {number_dictionary[4]} | {number_dictionary[5]} | {number_dictionary[6]} \n" \
                    f"---|---|---\n {number_dictionary[7]} | {number_dictionary[8]} | {number_dictionary[9]} "
    # Shows current game board using most recent replacement
    print(f"Here is your current game board: \n{current_board}")

    return number_dictionary, current_board


def x_or_o():
    # Assign X and O to Player1 and Player2
    global player1
    global player2
    assignment = True
    player1 = input("Welcome to TicTacToe! Player 1, would you like to be X or O? ")
    while assignment:
        if player1.upper() == "X" or player1.upper() == "O":
            assignment = False
        else:
            player1 = input("Sorry, that is not an X or O. Please try again: ")

    player1 = player1.upper()

    if player1 == "X":
        player2 = "O"
        print(f"Player 2 will be {player2}.")
    if player1 == "O":
        player2 = "X"
        print(f"Player 2 will be {player2}.")

    # Ask players if they are ready to begin
    asking_ready = True
    ready = input("Great! Are you ready to play? Y or N: ")
    while asking_ready:
        if ready.upper() != "Y" and ready.upper() != "N":
            ready = input("Sorry, that is not a Y or N. Please try again: ")
        if ready.upper() == "Y":
            print("Let's begin.")
            asking_ready = False
        if ready.upper() == "N":
            ready = input("Are you ready to play now? Y or N: ")

    return player1, player2


def choose_position(player1, player2):
    # Player chooses where to put their letter
    global player
    global player_choice
    choosing = True
    # Checking if Player1 or Player2 is choosing this turn.
    if player % 2 == 1:
        player_choice = input(f"Player1, choose a box to put an {player1}: ")
    if player % 2 == 0:
        player_choice = input(f"Player2, choose a box to put an {player2}: ")

    # Validating user input
    while choosing:
        if player_choice.isdigit():
            player_choice = int(player_choice)
            if player_choice not in numbers:
                player_choice = input(f"Sorry, that is not in the remaining boxes to choose from ({numbers}). Please "
                                      f"try again: ")
            if player_choice in numbers:
                numbers.remove(player_choice)
                print("Great!")
                choosing = False
        else:
            player_choice = input("Sorry, that is not a number. Please try again: ")

    return player, player_choice


def replacement(player, player_choice):
    global number_dictionary
    # Checks which player's turn it is and executes the replacement on the game board
    if player % 2 == 1:
        number_dictionary[player_choice] = player1
    if player % 2 == 0:
        number_dictionary[player_choice] = player2

    return number_dictionary


def check_tictactoe(number_dictionary, current_board):
    # Checks for 3 in a row (tic-tac-toe)
    if number_dictionary[1] == number_dictionary[2] == number_dictionary[3] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[1] == number_dictionary[2] == number_dictionary[3] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[4] == number_dictionary[5] == number_dictionary[6] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[4] == number_dictionary[5] == number_dictionary[6] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[7] == number_dictionary[8] == number_dictionary[9] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[7] == number_dictionary[8] == number_dictionary[9] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[1] == number_dictionary[4] == number_dictionary[7] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[1] == number_dictionary[4] == number_dictionary[7] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[2] == number_dictionary[5] == number_dictionary[8] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[2] == number_dictionary[5] == number_dictionary[8] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[3] == number_dictionary[6] == number_dictionary[9] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[3] == number_dictionary[6] == number_dictionary[9] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[1] == number_dictionary[5] == number_dictionary[9] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[1] == number_dictionary[5] == number_dictionary[9] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    if number_dictionary[3] == number_dictionary[5] == number_dictionary[7] == player1:
        current_board = game_board()[1]
        print("Player1 wins!")
        return False
    if number_dictionary[3] == number_dictionary[5] == number_dictionary[7] == player2:
        current_board = game_board()[1]
        print("Player2 wins!")
        return False
    else:
        return True


def still_playing():
    global playing
    global repeat
    # Checks if someone has won, so we will ask if they want to play again.
    if not check_tictactoe(number_dictionary, current_board):
        asking_again = True
        again = input("Do you want to play again? Y or N: ")
        while asking_again:
            if again.upper() != "Y" and again.upper() != "N":
                again = input("Sorry, that is not a Y or N. Please try again: ")
            if again.upper() == "Y":
                print("Let's play again!")
                asking_again = False
                playing = False
                repeat = True
                return playing, repeat
            if again.upper() == "N":
                print("Goodbye!")
                playing = False
                repeat = False
                return repeat
    # Next checks if the board is full, so we will ask if they want to play again.
    if numbers == []:
        asking_again = True
        again = input("No moves left - it's a tie! Do you want to play again? Y or N: ")
        while asking_again:
            if again.upper() != "Y" and again.upper() != "N":
                again = input("Sorry, that is not a Y or N. Please try again: ")
            if again.upper() == "Y":
                print("Let's play again!")
                asking_again = False
                playing = False
                repeat = True
                return playing, repeat
            if again.upper() == "N":
                print("Goodbye!")
                playing = False
                repeat = False
                return repeat
    # If no one has won yet, we ask users if they want to keep playing.
    asking_to_continue = True
    keep_playing = input("Do you want to keep playing? Y or N: ")
    while asking_to_continue:
        if keep_playing.upper() != "Y" and keep_playing.upper() != "N":
            keep_playing = input("Sorry, that is not a Y or N. Please try again: ")
        if keep_playing.upper() == "Y":
            print("Great! Next turn.")
            asking_to_continue = False
            playing = True
        if keep_playing.upper() == "N":
            print("Okay!")
            asking_to_continue = False
            playing = False

    return playing


while repeat:
    # Beginning of loop if user chooses to play again; resets all variables
    playing = True
    number_dictionary = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    current_board = f" {number_dictionary[1]} | {number_dictionary[2]} | {number_dictionary[3]} \n" \
                    f"---|---|---\n {number_dictionary[4]} | {number_dictionary[5]} | {number_dictionary[6]} \n" \
                    f"---|---|---\n {number_dictionary[7]} | {number_dictionary[8]} | {number_dictionary[9]} "
    player = 0
    player1 = ""
    player2 = ""
    player_choice = ""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x_or_o()
    print(f"Here is how you will specify which box to put your letter in: \n{numbered_board}")
    while playing:
        game_board()
        player += 1
        choose_position(player1, player2)
        replacement(player, player_choice)
        still_playing()
