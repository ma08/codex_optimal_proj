

def main():
    n, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    total_profit = 0
    days = [0] * k

    for i in range(n):
        j = (i % k)
        days[j] += 1
        if a[i] > total_profit:
            total_profit = a[i]

    print(total_profit)
    print(' '.join(map(str, days)))


if __name__ == '__main__':
    main()