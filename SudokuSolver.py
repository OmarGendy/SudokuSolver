import os


def check_row(x, grid):
    """
    Checks the row of a selected coordinate to see if the coordinate can be solved
    :param grid: The sudoku 2D array
    :param x: Row that needs to be checked in the grid
    :return: Number the box can be filled in as, or 0 if it cannot be solved
    """

    num_checker = [0, False, False, False, False, False, False, False, False, False]
    solution = 0

    # Check what numbers exist in the row
    for i in range(0, 9):
        num_checker[grid[x][i]] = True

    # If the row is solvable, num_checker will be a list of 9 Trues (includes 0) and 1 False who's index will be the solution.
    if num_checker.count(False) == 1:
        for i in range(1, 10):
            if not num_checker[i]:
                solution = i
                break

    # Will return 0 if not solvable, thereby not altering the value in the grid
    return solution


def check_column(y, grid):
    """
    Checks the row of a selected coordinate to see if the coordinate can be solved
    :param grid: The sudoku 2D array
    :param y: Column that needs to be checked in the grid
    :return: Number the box can be filled in as, or 0 if it cannot be solved
    """

    num_checker = [0, False, False, False, False, False, False, False, False, False]
    solution = 0

    # Check what numbers exist in the column
    for i in range(0, 9):
        num_checker[grid[i][y]] = True

    # If the column is solvable, num_checker will be a list of 9 Trues (includes 0) and 1 False who's index will be the solution.
    if num_checker.count(False) == 1:
        for i in range(1, 10):
            if not num_checker[i]:
                solution = i
                break

    # Will return 0 if not solvable, thereby not altering the value in the grid
    return solution


def main():
    # os.chdir(os.path.expanduser('~'))
    # filepath = input("Please provide the full path to your sudoku board .txt file\n\
    # For example: \"C:\\Users\\User\\Documents\\sudokuboard.txt\"")
    # # This will force the user to type a path of an existing .txt file
    # while not os.path.exists(filepath) and not os.path.splitext(filepath)[1] == ".txt":
    #     filepath = input("I did not find your file there. Please retry entering a path: ")

    filepath = "C:\\Users\\akama\\Documents\\sudokuboard.txt"
    board_file = open(filepath, "r")
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # Populate the grid with values from the .txt file (11 lines). Removes spaces and | to condense line to just values
    for x in range(0, 9):
        curr_line = board_file.readline()
        if curr_line[0] == '-':
            # Skip over the lines with dashes
            curr_line = board_file.readline()
        curr_line = curr_line.replace("|", "")
        curr_line = curr_line.replace(" ", "")
        for y in range(0, 9):
            grid[x][y] = int(curr_line[y])


if __name__ == "__main__":
    main()
