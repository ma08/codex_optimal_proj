

def main():
    # Get input
    n, t = [int(x) for x in input().split()]
    times = [int(x) for x in input().split()]
    total = 0
    for time in times:
        total += time
        if total > t:
            print(times.index(time))
            break
    else:
        print(n)

if __name__ == '__main__':
    main()
