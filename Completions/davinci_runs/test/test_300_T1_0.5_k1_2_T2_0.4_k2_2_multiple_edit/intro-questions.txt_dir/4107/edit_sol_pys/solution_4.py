

def main():
    # Read input
    n, k = [int(i) for i in input().split()]
    s = input()

    # Initialize the array to store the cost of placing a router in the room.
    # If a router is placed in the room, the cost is the index of the room.
    cost = [i + 1 for i in range(n) if s[i] == '1']

    # Update the cost based on the router's range.
    # If a router is placed in the room, the cost is the minimum cost of the room and the room's cost.
    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost.
    total_cost = sum(cost)

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
