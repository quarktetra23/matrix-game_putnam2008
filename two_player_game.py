import numpy as np

def display_matrix(matrix):
    print("\nCurrent Matrix:")
    for row in matrix:
        print(row)

def check_winner(matrix, player1, player2):
    det = np.linalg.det(matrix)
    print(f"\nDeterminant of the matrix: {det:.6f}")
    if det == 0:
        return f"{player2} wins (determinant is 0)!"
    else:
        return f"{player1} wins (determinant is non-zero)!"

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value not in valid_range:
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. Please enter a number between {valid_range.start} and {valid_range.stop - 1}.")

def get_real_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")

def play_game(size, player1, player2):
    matrix = np.zeros((size, size))  # Create a size x size matrix filled with zeros
    filled_positions = set()  # Track filled positions

    players = [player1, player2]
    turn = 0  # Player 1 starts first

    while len(filled_positions) < size * size:
        current_player = players[turn % 2]
        display_matrix(matrix)
        print(f"{current_player}'s turn.")

        # Get valid row and column input
        row = get_valid_input(f"Enter row (0 to {size-1}): ", range(0, size))
        col = get_valid_input(f"Enter column (0 to {size-1}): ", range(0, size))

        # Ensure the position is vacant
        while (row, col) in filled_positions:
            print("This position is already filled. Try again.")
            row = get_valid_input(f"Enter row (0 to {size-1}): ", range(0, size))
            col = get_valid_input(f"Enter column (0 to {size-1}): ", range(0, size))

        # Get a valid real number
        value = get_real_number("Enter a real number to place: ")
        matrix[row][col] = value
        filled_positions.add((row, col))

        turn += 1

    # Final matrix display
    display_matrix(matrix)

    # Determine the winner and print the determinant
    return check_winner(matrix, player1, player2)

if __name__ == "__main__":
    print("Welcome to the Alan vs. Barbara 2008 matrix game!")

    # Allow players to input their names
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    size = get_valid_input("Enter the size of the square matrix (e.g., 3 for 3x3): ", range(1, 101))  # Limiting the matrix size to 1 to 100 for practical reasons
    print(play_game(size, player1, player2))
