

def main():
    # read input and convert to integers
    n, k = map(int, input().split())

    # read input and convert to integers
    s = list(map(int, input().split()))

    # initialize the array to store the cost of placing a router in the room and the cost of placing a router in the room
    cost = [0] * n  # cost of placing a router in the room
    total_cost = 0  # total cost

    for i in range(n):
        if s[i] == 1:
            cost[i] = i + 1
            total_cost += cost[i]

    # update the cost based on the routers' range and update the total cost
    for i in range(k, n):
        if s[i] == 1:
            cost[i] = min(cost[i], cost[i - k] + i + 1)
            total_cost += cost[i]

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
