

def main():
    n, k = map(int, input().split())  # n is number of days, k is number of workers
    a = [int(x) for x in input().split()]  # a is the list of profits for each day
    total_profit = 0
    days = [0] * k

    for i in range(n):
        days[i % k] += 1
        if a[i] > total_profit:
            total_profit = a[i]

    print(total_profit)
    print(' '.join(map(str, days)))


if __name__ == '__main__':
    main()
