

def main():
    n, k = map(int, input().split())  # n is the number of days, k is the number of days per week.
    a = [int(x) for x in input().split()]  # a is the list of profits.
    total_profit = 0  # total profit.
    days = [0] * k  # days is the list of days per week.

    for i in range(n):
        j = (i % k)  # j is the index of days.
        days[j] += 1  # increase the value of days[j] by 1.
        if a[i] > total_profit:  # if the profit of day i is greater than total profit.
            total_profit = a[i]  # then total profit is the profit of day i.

    print(total_profit)  # print the total profit.
    print(' '.join(map(str, days)))  # print the days per week.


if __name__ == '__main__':
    main()
