
def main():
    n = int(input())
    times = [int(x) for x in input().split()]  # list comprehension

    times.sort()

    total = 0
    for i in range(n):
        total += (n - i) * times[i]

    print(total)


if __name__ == "__main__":
    main()
