

def main():
    # read input
    n, k = [int(i) for i in input().split()]
    s = input()

    # initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i in range(n):
        if s[i] == '1':
            cost[i] = i + 1

    # update the cost based on the routers' range.
    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # sum the cost
    total_cost = sum(cost)

    # output
    print(total_cost)


if __name__ == "__main__":
    main()
