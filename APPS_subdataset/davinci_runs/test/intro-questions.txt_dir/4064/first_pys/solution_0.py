

def main():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))

    # Time starts at 0, so we can subtract 1 from the time for each sleep
    for i in range(n):
        a[i] -= 1

    # Initialize the first time to be bad
    good = [0]
    for i in range(n):
        time = a[i] % h
        if l <= time <= r:
            good.append(good[-1] + 1)
        else:
            good.append(good[-1])

    # Initialize the first time to be good
    bad = [0]
    for i in range(n):
        time = a[i] % h
        if l <= time <= r:
            bad.append(bad[-1])
        else:
            bad.append(bad[-1] + 1)

    # We want to maximize the number of good times, so we check which is better
    print(max(good[n], bad[n]))

if __name__ == "__main__":
    main()