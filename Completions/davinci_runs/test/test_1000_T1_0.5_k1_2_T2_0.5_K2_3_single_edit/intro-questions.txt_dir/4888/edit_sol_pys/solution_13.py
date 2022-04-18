

def main():
    # Get input
    n, t = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    # Iterate through tasks and see if they can be completed
    total = 0
    for time in times:
        total += time
        if total > t:
            print(times.index(time) + 1)
            break
    else:
        print(n)

if __name__ == '__main__':
    main()
