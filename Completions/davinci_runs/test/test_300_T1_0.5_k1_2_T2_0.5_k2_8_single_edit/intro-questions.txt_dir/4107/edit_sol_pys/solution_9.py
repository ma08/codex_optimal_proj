"""
Solution for the first problem in the second pair of advent of code problems
"""


def main():
    """
    Main function that parses input and runs the solution
    """
    # Read input
    with open('input.txt') as input_file:
        n, k = [int(i) for i in input_file.readline().split()]
        s = input_file.readline()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i in range(n):
        if s[i] == '1':
            cost[i] = i + 1

    # Update the cost based on the routers' range
    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost
    total_cost = sum(cost)

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
