

def main():
    # Read input from file
    with open('./file.txt', 'r') as f:
        n, k = [int(i) for i in f.readline().split()]
        s = f.readline()

    # Initialize the array to store the cost of placing a router in the room
    cost = [0] * n
    for i in range(n):
        if s[i] == '1':
            cost[i] = i + 1

    # Update the cost based on the routers' range
    for i in range(k, n):
        cost[i] = min(cost[i], cost[i - k] + i + 1)

    # Sum the cost
    total_cost = sum(cost)

    # Write output to file
    with open('./file_out.txt', 'w') as f:
        f.write(str(total_cost))


if __name__ == "__main__":
    main()
