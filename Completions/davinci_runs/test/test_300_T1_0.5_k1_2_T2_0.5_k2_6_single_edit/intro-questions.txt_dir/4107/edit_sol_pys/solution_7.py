

def main():
    # Read input
    n, k = map(int, input().split())
    s = list(input())

    # Initialize the array to store the cost of placing a router in the room
    cost = [0 for i in range(n)]
    for i in range(n):
        cost[i] = i + 1

    # Update the cost based on the routers' range
    for i in range(1, n):
        if s[i] == '1':
            cost[i] = min(cost[i], cost[i - 1] + i + 1)
        else:
            cost[i] = cost[i - 1]

    # Sum the cost
    total_cost = cost[n - 1]

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
