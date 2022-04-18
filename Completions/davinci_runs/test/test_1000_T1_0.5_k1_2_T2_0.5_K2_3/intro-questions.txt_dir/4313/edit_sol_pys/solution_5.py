

def main():
    n = int(input())
    values = [int(x) for x in input().split(" ")]
    costs = [int(x) for x in input().split(" ")]
    max_value = 0
    for i in range(1, 2**n):
        value = 0
        cost = 0
        for j in range(n):
            if ((i >> j) & 1):
                value += values[j]
                cost += costs[j]
        max_value = max(max_value, value - cost)
    print(max_value)


if __name__ == '__main__':
    main()
