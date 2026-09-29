
import random


def display_board(board):
    print()
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    empty_cells = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                empty_cells.append((i, j))

    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = "O"


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("TIC-TAC-TOE")
    print("You are X and the computer is O.")
    display_board(board)

    while True:
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid position! Enter values between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("That cell is already occupied!")
                continue

            board[row][col] = "X"

        except ValueError:
            print("Please enter numbers only.")
            continue

        display_board(board)

        if check_winner(board, "X"):
            print("Congratulations! You won!")
            break

        if board_full(board):
            print("It's a draw!")
            break

        print("Computer's turn...")
        computer_move(board)
        display_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if board_full(board):
            print("It's a draw!")
            break


play_game()
