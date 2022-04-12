

def main():
    # Read input and store in variables
    n, k = [int(i) for i in input().split()]  # n = number of rooms, k = range of router
    s = input()  # s = string of rooms

    # Initialize the array to store the cost of placing a router in the room.
    # The cost of placing a router in a room with no router is 0.
    cost = [0] * n  # cost = array of cost
    for i in range(n):
        if s[i] == '1':  # If the room has a router, the cost is the room number (i + 1)
            cost[i] = i + 1  # cost[i] = cost of placing a router in room i

    # Update the cost based on the router's range.
    # The cost of placing a router in a room with a router is the minimum of the cost of placing a router in the room
    # and the cost of placing a router in the previous room (i - k) + the room number (i + 1)
    for i in range(k, n):  # Loop through the rooms
        cost[i] = min(cost[i], cost[i - k] + i + 1)  # cost[i] = minimum of cost[i] and cost[i - k] + i + 1

    # Sum the cost.
    total_cost = sum(cost)  # total_cost = sum of cost

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
