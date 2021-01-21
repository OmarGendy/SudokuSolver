import os


def solve_coord(x, y, grid):
    """
    Checks the row, column, and box of a selected coordinate to see if it can be solved
    :param x & y: Coordinate that needs to be solved in the grid
    :param grid: Reference to the sudoku 2D array
    :return: Number the box can be filled in as, or 0 if it cannot be solved
    """

    num_checker = [0, False, False, False, False, False, False, False, False, False]
    solution = 0

    # Check what numbers exist in the row
    for i in range(0, 9):
        num_checker[grid[x][i]] = True

    # num_checker will populate with True for numbers (the indexes 1-9) that exist in the row
    if num_checker.count(False) == 1:
        for i in range(1, 10):
            if not num_checker[i]:
                solution = i
                break

    # Check what numbers exist in the column
    for i in range(0, 9):
        num_checker[grid[i][y]] = True

    # num_checker will populate with True for numbers (the indexes 1-9) that exist in the column
    if num_checker.count(False) == 1:
        for i in range(1, 10):
            if not num_checker[i]:
                solution = i
                break

    # Determines which box we're dealing with (1-9), then populates num_checker based on values.
    if x <= 2 and y <= 2:  # Box 1
        for i in range(0, 3):
            for j in range(0, 3):
                num_checker[grid[i][j]] = True

    elif x <= 2 and 3 <= y <= 5:  # Box 2
        for i in range(0, 3):
            for j in range(3, 6):
                num_checker[grid[i][j]] = True
    elif x <= 2 and y >= 6:  # Box 3
        for i in range(0, 3):
            for j in range(6, 9):
                num_checker[grid[i][j]] = True
    elif 3 <= x <= 5 and y <= 2:  # Box 4
        for i in range(3, 6):
            for j in range(0, 3):
                num_checker[grid[i][j]] = True
    elif 3 <= x <= 5 and 3 <= y <= 5:  # Box 5
        for i in range(3, 6):
            for j in range(3, 6):
                num_checker[grid[i][j]] = True
    elif 3 <= x <= 5 and y >= 6:  # Box 6
        for i in range(3, 6):
            for j in range(6, 9):
                num_checker[grid[i][j]] = True
    elif x >= 6 and y <= 2:  # Box 7
        for i in range(6, 9):
            for j in range(0, 3):
                num_checker[grid[i][j]] = True
    elif x >= 6 and 3 <= y <= 5:  # Box 8
        for i in range(6, 9):
            for j in range(3, 6):
                num_checker[grid[i][j]] = True
    elif x >= 6 and y >= 6:  # Box 9
        for i in range(6, 9):
            for j in range(6, 9):
                num_checker[grid[i][j]] = True

    # If the box is solvable, num_checker will be a list of 9 Trues (includes 0) and 1 False who's index will be the solution.
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
    with open(filepath, "r") as board_file:
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

    # Begin solving
    while 0 in grid[0] or 0 in grid[1] or 0 in grid[2] or 0 in grid[3] or 0 in grid[4] or 0 in grid[5] or 0 in grid[6] or 0 in grid[7] or 0 in grid[8]:
        for x in range(0, 9):
            for y in range(0, 9):
                if grid[x][y] == 0:
                    grid[x][y] = solve_coord(x, y, grid)

    # Outputting solution to new file in same directory as original file
    os.chdir(os.path.split(filepath)[0])
    with open("sudoku_solved.txt", "w") as new_file:
        for i in range(0, 9):

            # Create a temp variable with string values instead of ints
            curr_list = grid[i]
            for j in range(0, 9):
                curr_list[j] = str(curr_list[j])

            # Format the string to look like the original .txt
            j = 1
            while j < 16:
                curr_list.insert(j, " ")
                j += 2
            curr_list.insert(6, "| ")
            curr_list.insert(13, "| ")
            line = "".join(curr_list)

            # Writing to file. No new line at last line and requires format rows.
            if i == 8:
                new_file.write(line)
            elif i == 2 or i == 5:
                new_file.write(line)
                new_file.write("\n")
                new_file.write("------+-------+------")
                new_file.write("\n")
            else:
                new_file.write(line)
                new_file.write("\n")

    # Printing result
    with open("sudoku_solved.txt", "r") as new_file:
        print(new_file.read())


if __name__ == "__main__":
    main()
