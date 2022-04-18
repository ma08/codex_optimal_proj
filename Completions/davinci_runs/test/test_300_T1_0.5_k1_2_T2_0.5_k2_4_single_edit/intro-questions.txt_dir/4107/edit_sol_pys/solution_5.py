

def main():
    # Get input
    n, k = [int(i) for i in input().split()]
    s = input()

    # Initialize the array to store the cost of placing a router in each room
    cost = [0] * n
    for i in range(n):
        if s[i] == '1':
            cost[i] = i + 1

    # Update the cost based on the routers' range of coverage
    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost of placing all the routers
    total_cost = sum(cost)

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
