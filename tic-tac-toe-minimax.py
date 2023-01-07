import math

# This function draws the current board state to the console.
# It takes in a 2D list representing the board, where empty spaces are represented by a single space character,
# X's are represented by the "X" string, and O's are represented by the "O" string.


def draw_board(board):
    # Print the rows of the board and each player's symbol formatted into the appropriate position
    print("   |   |")
    print(" {} | {} | {}".format(board[0][0], board[0][1], board[0][2]))
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" {} | {} | {}".format(board[1][0], board[1][1], board[1][2]))
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" {} | {} | {}".format(board[2][0], board[2][1], board[2][2]))
    print("   |   |")


# This function checks if a player has won by filling a row with their symbol.
# It returns True if the player has won by filling a row, and False otherwise.


def check_row_win(board, player):
    for row in board:
        if row == [player, player, player]:
            return True
    return False


# This function checks if a player has won by filling a column with their symbol.
# It returns True if the player has won by filling a column, and False otherwise.


def check_col_win(board, player):
    for col in range(3):
        if (
            board[0][col] == player
            and board[1][col] == player
            and board[2][col] == player
        ):
            return True
    return False


# This function checks if a player has won by filling a diagonal with their symbol.
# It returns True if the player has won by filling a column, and False otherwise.


def check_diag_win(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


# This function checks if a player has won.
# It returns True if the player has won, and False otherwise.


def check_win(board, player):
    return (
        check_row_win(board, player)
        or check_col_win(board, player)
        or check_diag_win(board, player)
    )


# This function checks if the game ends in a draw.
# It returns True if there is a draw, and False otherwise.


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


# This function performs the minimax algorithm for the AI to determine the most optimal next move.
# It returns `value`` and `move`, where `value` is the heuristic value of the most optimal 'move' (row and column).


def minimax(board, depth, player, maximizing_player):
    result = check_win(board, "X")
    if result:
        return (-1, None)
    result = check_win(board, "O")
    if result:
        return (1, None)
    result = check_draw(board)
    if result:
        return (0, None)
    if maximizing_player:
        value = -math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    new_value, _ = minimax(
                        board, depth + 1, "O" if player == "X" else "X", False
                    )
                    board[i][j] = " "
                    if new_value > value:
                        value = new_value
                        move = (i, j)
        return (value, move)
    else:
        value = math.inf
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    new_value, _ = minimax(
                        board, depth + 1, "O" if player == "X" else "X", True
                    )
                    board[i][j] = " "
                    if new_value < value:
                        value = new_value
                        move = (i, j)
        return (value, move)


# This function initializes and executes the tic-tac-toe game.


def main():
    # Initializing the board.
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    # Prompts the player to choose whether they would like to go first, as "X", or second, as "O".
    while True:
        choice = input("Do you want to go first? (Y/n) ").lower()
        if choice == "y":
            player = "X"
            break
        elif choice == "n":
            player = "O"
            break
        else:
            print("Invalid input! Please enter 'Y' or 'n'.")
    while True:
        if player == "X":
            # Play the game by prompting for player to choose a row number (1-3) and a column number (1-3).
            draw_board(board)
            while True:
                row, col = tuple(
                    map(
                        int,
                        input("Enter 'row' and 'column' separated by a comma: ").split(
                            ","
                        ),
                    )
                )
                row = row - 1
                col = col - 1
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Please enter a valid row and column number.")
                elif board[row][col] != " ":
                    print("That space is already occupied! Try again.")
                else:
                    break
        else:
            # Play the game by invoking minimax algorithm to play the AI's turn.
            print("AI's turn...")
            value, move = minimax(board, 0, player, True)
            row, col = move
        board[row][col] = player

        # Check for a winning case.
        if check_win(board, player):
            draw_board(board)
            print("{} wins!".format(player))
            break
        # Check for a draw case.
        if check_draw(board):
            draw_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"


main()
