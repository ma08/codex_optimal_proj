

def main():
    """
    This is the main function that runs the program.
    """
    # Get user input
    dimensions = input().strip().split()
    m = int(dimensions[0])
    n = int(dimensions[1])
    heights = []
    for _ in range(m):
        heights.append(list(map(int, input().strip().split())))
    # Get the minimum ladder length
    minimum_ladder_length = min_ladder_length(heights, m, n)
    # Print the results
    print(minimum_ladder_length)

def min_ladder_length(heights, m, n):
    """
    Calculate the minimum ladder length required to
    reach the bottom right corner from the top left
    corner of the grid.
    """
    # Initialize a 2D array to store the minimum ladder lengths at each position
    minimum_ladder_lengths = [[float("inf") for _ in range(n)] for __ in range(m)]
    # Set the minimum ladder length at the top left corner as 0
    minimum_ladder_lengths[0][0] = 0
    # Initialize a queue to store the positions to be processed
    queue = []
    # Add the top left corner to the queue
    queue.append((0, 0))
    # While the queue is not empty
    while queue:
        # Get the current position
        current_position = queue.pop(0)
        # Get the current height
        current_height = heights[current_position[0]][current_position[1]]
        # Get the current minimum ladder length
        current_minimum_ladder_length = minimum_ladder_lengths[current_position[0]][current_position[1]]
        # Get the possible adjacent positions
        adjacent_positions = get_adjacent_positions(current_position, m, n)
        # For each adjacent position
        for adjacent_position in adjacent_positions:
            # Get the adjacent height
            adjacent_height = heights[adjacent_position[0]][adjacent_position[1]]
            # If the adjacent height is greater than the current height
            if adjacent_height > current_height:
                # Calculate the adjacent minimum ladder length
                adjacent_minimum_ladder_length = current_minimum_ladder_length + adjacent_height - current_height
            else:
                # Calculate the adjacent minimum ladder length
                adjacent_minimum_ladder_length = current_minimum_ladder_length
            # If the adjacent minimum ladder length is less than the existing minimum ladder length
            if adjacent_minimum_ladder_length < minimum_ladder_lengths[adjacent_position[0]][adjacent_position[1]]:
                # Update the adjacent minimum ladder length
                minimum_ladder_lengths[adjacent_position[0]][adjacent_position[1]] = adjacent_minimum_ladder_length
                # Add the adjacent position to the queue
                queue.append(adjacent_position)
    # Return the minimum ladder length at the bottom right corner
    return minimum_ladder_lengths[m - 1][n - 1]

def get_adjacent_positions(current_position, m, n):
    """
    Get the possible adjacent positions of the current
    position.
    """
    # Initialize a list to store the adjacent positions
    adjacent_positions = []
    # If the current position is not on the top row
    if current_position[0] > 0:
        # Add the position above the current position
        adjacent_positions.append((current_position[0] - 1, current_position[1]))
    # If the current position is not on the bottom row
    if current_position[0] < m - 1:
        # Add the position below the current position
        adjacent_positions.append((current_position[0] + 1, current_position[1]))
    # If the current position is not on the leftmost column
    if current_position[1] > 0:
        # Add the position to the left of the current position
        adjacent_positions.append((current_position[0], current_position[1] - 1))
    # If the current position is not on the rightmost column
    if current_position[1] < n - 1:
        # Add the position to the right of the current position
        adjacent_positions.append((current_position[0], current_position[1] + 1))
    # Return the adjacent positions
    return adjacent_positions

if __name__ == "__main__":
    main()
