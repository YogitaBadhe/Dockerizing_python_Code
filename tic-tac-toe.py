# tic_tac_toe.py
import os

# Function to print the board
def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tic-Tac-Toe Game\n")
    for i in range(3):
        print("|", " | ".join(board[i]), "|")
        if i != 2:
            print("-" * 9)

# Function to check if someone won
def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Main game function
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    turns = 0
    
    while turns < 9:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Cell is already occupied! Try again.")
                continue
            board[row][col] = current_player
            turns += 1
            
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input! Please enter valid row and column numbers between 0-2.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()
