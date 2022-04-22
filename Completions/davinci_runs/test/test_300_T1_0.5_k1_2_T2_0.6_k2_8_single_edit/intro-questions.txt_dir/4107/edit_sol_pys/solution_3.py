

def main():
    # Read input
    n, k = [int(i) for i in input().split()]
    s = input()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i, c in enumerate(s):
        if c == '1':
            cost[i] = i + 1 - k

    # Update the cost based on the routers' range
    for i in range(1, n):
        cost[i] = min(cost[i], cost[i - 1] + 1)

    # Sum the cost
    total_cost = sum(cost)

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
