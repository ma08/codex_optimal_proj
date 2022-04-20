

def main():
    # Read input
    n, k = [int(i) for i in input().split()]  # n: number of rooms, k: range of router
    s = input()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i in range(n):
        if s[i] == '1':  # there is a router in the room
            cost[i] = i + 1

    # Update the cost based on the routers' range
    for i in range(k, n):  # start from the k-th room
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost
    total_cost = sum(cost)  # sum the cost of placing routers in all rooms

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
