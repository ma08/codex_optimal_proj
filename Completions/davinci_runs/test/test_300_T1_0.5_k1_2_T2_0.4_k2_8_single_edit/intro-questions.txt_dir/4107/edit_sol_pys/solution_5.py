

def main():
    # Read input
    n, k = [int(i) for i in input().split()]  # number of rooms and router range
    s = input()  # rooms with routers already installed

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n  # cost of placing a router in the room
    for i in range(n):
        if s[i] == '1':  # if router is already installed, cost is 0
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
