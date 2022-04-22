

def main():
    # Read input

    n, k = [int(i) for i in input().split()]
    s = input()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i, room in enumerate(s):
        if room == '1':
            cost[i] = i + 1

    # Update the cost based on the routers' range
    for i in range(k, n):  # For each room
        cost[i] = min(cost[i], cost[i - k] + i + 1)  # Update the cost

    # Sum the cost
    total_cost = sum(cost)  # Sum the cost

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
