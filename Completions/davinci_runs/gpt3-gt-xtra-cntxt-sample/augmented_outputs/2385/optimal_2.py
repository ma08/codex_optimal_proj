t = int(input())

for case in range(t):
    n, m = map(int, input().split())

    # Create a 2D array to store the color of each cell
    colors = []
    for i in range(n):
        colors.append(input())

    # Create a 2D array to store the direction of each cell
    directions = []
    for i in range(n):
        directions.append(input())

    # List to store the number of black cells occupied by the robots before all movements
    black_count = []

    # List to store the number of robots placed
    robot_count = []

    # Loop through each cell
    for i in range(n):
        for j in range(m):
            # If the cell is black
            if colors[i][j] == "0":
                # If the robot can move to the right
                if j + 1 < m and directions[i][j] == "R":
                    # If the cell to the right is black
                    if colors[i][j + 1] == "0":
                        # Place the robot in the cell
                        colors[i][j] = "2"
                        # Place the robot in the cell to the right
                        colors[i][j + 1] = "2"
                        # Increment the number of robots placed
                        robot_count.append(1)
                        # Increment the number of black cells occupied by the robots before all movements
                        black_count.append(2)
                # If the robot can move down
                if i + 1 < n and directions[i][j] == "D":
                    # If the cell below is black
                    if colors[i + 1][j] == "0":
                        # Place the robot in the cell
                        colors[i][j] = "2"
                        # Place the robot in the cell below
                        colors[i + 1][j] = "2"
                        # Increment the number of robots placed
                        robot_count.append(1)
                        # Increment the number of black cells occupied by the robots before all movements
                        black_count.append(2)

    # Print the maximum number of robots placed
    print(max(robot_count), max(black_count))