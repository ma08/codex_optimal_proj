
def main():
    n = int(input()) # number of people
    times = [int(x) for x in input().split()] # times for each person

    # sort times in ascending order
    times.sort()
        # add the time for each person to the total

    total = 0
    for i in range(n):
        total += (n - i) * times[i]

    print(total)


if __name__ == '__main__':
    main()
