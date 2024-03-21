# This program implements an interactive two-player game of Tic-Tac-Toe
#
# Module 2 Project
# @author - Addie Domanico - CPSC4970 - AO3
# @version - 03/24/2024

def initialize_board():
    # Initializes an empty 3x3 board
    return [[' ' for _ in range(3)] for _ in range(3)]


def print_board(board):
    # Prints the current state of the board
    print("  1   2   3")
    for i in range(3):
        print(f"{i + 1} {' | '.join(board[i])}")
        if i != 2:
            print("  --+---+--")


def check_winner(board):
    # Checks if there is a winner or if it is a draw
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True, row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True, board[0][2]

    if all(cell != ' ' for row in board for cell in row):
        return True, 'Draw'
    return False, None


def get_move(player):
    # Determines if player entered a valid move
    while True:
        move = input(f"Enter {player} move (row, column no spaces)> ")
        try:
            row, col = map(int, move.split(','))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid move, try again.")


def valid_move(board, row, col):
    # Checks if the move is valid (empty cell available)
    return board[row][col] == ' '


def play_game():
    # Main game loop
    board = initialize_board()
    players = ['X', 'O']
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]

        while True:
            row, col = get_move(player)

            if valid_move(board, row, col):
                board[row][col] = player
                winner_found, winner = check_winner(board)
                if winner_found:
                    print_board(board)
                    if winner == 'Draw':
                        print("\nIt's a draw!")
                    else:
                        print(f"\n{winner} is the winner!")
                    return
                turn += 1
                break
            else:
                print("Invalid move, try again.")


def main():
    # Entry point of program
    play_game()

if __name__ == '__main__':
    main()
