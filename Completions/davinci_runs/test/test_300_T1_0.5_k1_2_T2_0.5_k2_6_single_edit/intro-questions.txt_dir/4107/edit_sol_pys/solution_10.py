

def main():
    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * 10
    for i in range(10):
        if i == 0:
            cost[i] = 0
        else:
            cost[i] = i

    # Update the cost based on the routers' range (k = 3)
    for i in range(3, 10):
        cost[i] = min(cost[i], cost[i - 3] + i)

    # Sum the cost
    total_cost = sum(cost) - cost[0]

    # Output
    print(total_cost)


if __name__ == "__main__":
    main()
