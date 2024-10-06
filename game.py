import numpy as np

def display_matrix(matrix):
    print("\nCurrent Matrix:")
    for row in matrix:
        print(row)

def check_winner(matrix):
    numeric_matrix = np.array(matrix, dtype=float)
    det = np.linalg.det(numeric_matrix)
    print(f"\nDeterminant of the matrix: {det:.6f}")
    if det == 0:
        return "Barbara wins (determinant is 0)!"
    else:
        return "Alan wins (determinant is non-zero)!"

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

def play_game(size):
    matrix = [['x' for _ in range(size)] for _ in range(size)]
    filled_positions = set()

    players = ['Alan', 'Barbara']
    turn = 0

    while len(filled_positions) < size * size:
        current_player = players[turn % 2]
        display_matrix(matrix)
        print(f"{current_player}'s turn.")

        row = get_valid_input(f"Enter row (0 to {size-1}): ", range(0, size))
        col = get_valid_input(f"Enter column (0 to {size-1}): ", range(0, size))

        while (row, col) in filled_positions:
            print("This position is already filled. Try again.")
            row = get_valid_input(f"Enter row (0 to {size-1}): ", range(0, size))
            col = get_valid_input(f"Enter column (0 to {size-1}): ", range(0, size))

        value = get_real_number("Enter a real number to place: ")
        matrix[row][col] = value
        filled_positions.add((row, col))

        turn += 1

    display_matrix(matrix)

    return check_winner(matrix)

if __name__ == "__main__":
    print("Welcome to the Alan vs. Barbara matrix game!")
    size = get_valid_input("Enter the size of the square matrix (e.g., 3 for 3x3): ", range(1, 51))
    print(play_game(size))
