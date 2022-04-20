

def main():
    # Read input
    n, k = [int(i) for i in input().split()] # n: number of rooms, k: range of router
    s = input() # s: string of room states

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n # cost: array of cost of placing a router in the room
    for i in range(n):
        if s[i] == '1': # if room is occupied
            cost[i] = i + 1 # cost of placing a router in the room is the room number

    # Update the cost based on the routers' range
    for i in range(k, n): # update cost of room i based on the cost of room i - k
        cost[i] = min(cost[i], cost[i - k] + i + 1) # cost of room i is the minimum of cost of room i and cost of room i - k + room i

    # Sum the cost
    total_cost = sum(cost) # total cost is the sum of cost of placing routers in all rooms

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
