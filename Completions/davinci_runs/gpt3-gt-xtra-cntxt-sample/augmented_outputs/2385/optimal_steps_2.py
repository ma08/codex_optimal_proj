import sys

# Get the number of test cases
t = int(sys.stdin.readline())

# Loop through each test case
for i in range(t):

    # Get the number of rows and columns in the grid
    n, m = map(int, sys.stdin.readline().split())

    # Initialize the number of black cells in the grid
    blackCells = 0

    # Initialize the number of white cells in the grid
    whiteCells = 0

    # Initialize the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
    robots = 0

    # Initialize the maximum number of black cells that can be occupied by robots before all movements
    maxBlackCells = 0

    # Loop through each row in the grid
    for j in range(n):

        # Get the current row in the grid
        row = sys.stdin.readline()

        # Loop through each column in the current row in the grid
        for k in range(m):

            # If the current cell in the grid is black
            if row[k] == '0':

                # Increment the number of black cells in the grid
                blackCells += 1

            # If the current cell in the grid is white
            elif row[k] == '1':

                # Increment the number of white cells in the grid
                whiteCells += 1

    # Loop through each row in the grid
    for j in range(n):

        # Get the current row in the grid
        row = sys.stdin.readline()

        # Loop through each column in the current row in the grid
        for k in range(m):

            # If the current cell in the grid is black
            if row[k] == '0':

                # If the current cell in the grid is in the top row
                if j == 0:

                    # Increment the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
                    robots += 1

                # If the current cell in the grid is in the bottom row
                elif j == n - 1:

                    # Increment the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
                    robots += 1

                # If the current cell in the grid is in the leftmost column
                elif k == 0:

                    # Increment the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
                    robots += 1

                # If the current cell in the grid is in the rightmost column
                elif k == m - 1:

                    # Increment the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
                    robots += 1

                # If the current cell in the grid is not in the top row, bottom row, leftmost column, or rightmost column
                else:

                    # Increment the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
                    robots += 2

    # If the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell is less than the number of white cells in the grid
    if robots < whiteCells:

        # Set the maximum number of black cells that can be occupied by robots before all movements to the number of black cells in the grid
        maxBlackCells = blackCells

    # If the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell is greater than or equal to the number of white cells in the grid
    else:

        # Set the maximum number of black cells that can be occupied by robots before all movements to the number of black cells in the grid minus the number of white cells in the grid plus the number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell
        maxBlackCells = blackCells - whiteCells + robots

    # Print the maximum number of robots that can be placed in the grid such that there is no move before which two different robots occupy the same cell and the maximum number of black cells that can be occupied by robots before all movements
    print(str(robots) + " " + str(maxBlackCells))