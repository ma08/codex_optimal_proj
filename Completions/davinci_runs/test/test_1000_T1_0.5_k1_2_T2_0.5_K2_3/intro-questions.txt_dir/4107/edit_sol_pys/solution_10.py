

def main():
    # Read input
    n, k = [int(i) for i in input().split()]  # Read input
    s = input()  # Read input

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n  # Initialize the array to store the cost of placing a router in the room
    for i in range(n):
        if s[i] == '1':  # Update the cost based on the router's range
            cost[i] = i + 1

    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost
    total_cost = sum(cost)  # Sum the cost

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
