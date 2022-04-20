

def main():
    # Read input
    n, k = [int(i) for i in input().split()]  # n is the number of rooms, k is the range of router
    s = input()  # s is the string that contains '0' for empty rooms and '1' for occupied rooms

    # Initialize the array to store the cost of placing a router in each room
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
