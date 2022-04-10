

def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    total_profit = 0
    days = [0] * k  # days is a list of the number of days each worker works

    for i in range(n):
        j = (i % k)  # j is the index of the worker
        days[j] += 1
        if a[i] > total_profit:
            total_profit = a[i]

    print(total_profit)
    print(' '.join(map(str, days)))


if __name__ == '__main__':
    main()
