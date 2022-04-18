
def main():
    # Get input
    n, t = map(int, input().split())
    times = map(int, input().split())
    # Iterate through tasks and see if they can be completed
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
