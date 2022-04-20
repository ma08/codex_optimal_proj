

def main():
    n, k = map(int, input().split())
    s = input()

    # We can use a greedy algorithm where we place routers at the first rooms where
    # there are spots for routers, and then connect the remaining rooms directly.
    # So the cost of the optimal solution is the sum of the costs of the direct
    # connections and the costs of the routers.

    # We can find the cost of the direct connections using prefix sums.
    direct = 0
    for i in range(n):
        if s[i] == '0':
            direct += i + 1

    # We can find the cost of the routers by counting the number of rooms in each
    # interval of length 2k+1, where we place a router.
    routers = 0
    intervals = [0] * n
    for i in range(n):
        if s[i] == '1':
            intervals[max(0, i - k)] += 1
            if i + k + 1 < n:
                intervals[i + k + 1] -= 1
    count = 0
    for i in range(n):
        count += intervals[i]
        if count > 0:
            routers += i + 1

    print(direct + routers)


if __name__ == "__main__":
    main()