

def main():
    n, k = map(int, input().split())

    # Initialize the array to store the cost of placing a router in the
    # room
    cost = [0] * n
    for i, s in enumerate(input()):
        if s == '1':
            cost[i] = i

    # Update the cost based on the routers' range
    for i in range(1, n):
        cost[i] = min(cost[i], cost[i - 1] + 1)
        if i >= k:
            cost[i] = min(cost[i], cost[i - k] + k)

    print(cost[n - 1])


if __name__ == "__main__":
    main()
