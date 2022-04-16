

def main():
    # Read input
    n, k = [int(i) for i in input().split()]
    s = input().strip()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * (n + 1)
    for i in range(n):
        if s[i - 1] == '1':
            cost[i] = i

    # Update the cost based on the routers' range
    for i in range(k, n + 1):
        cost[i] = min(cost[i], cost[i - k] + i)

    # Sum the cost
    total_cost = sum(cost)

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
