import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

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

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are Player X. Computer is O.\n")

    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            try:
                row = int(input("Your move! Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input. Use numbers only.")
                continue

            if row not in range(3) or col not in range(3):
                print("Invalid position. Use 0, 1, or 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken.")
                continue
        else:
            print("Computer's turn...")
            row, col = get_computer_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            winner = "You" if current_player == "X" else "Computer"
            print(f"🎉 {winner} win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
