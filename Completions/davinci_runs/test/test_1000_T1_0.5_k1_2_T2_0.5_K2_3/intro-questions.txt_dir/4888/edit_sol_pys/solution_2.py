import sys


def main():
    # Get input.
    n, t = [int(x) for x in sys.stdin.readline().split()]
    times = [int(x) for x in sys.stdin.readline().split()]
    # Iterate through tasks and see if they can be completed.
    total = 0
    for time in times:
        total += time
        if total > t:
            sys.stdout.write(str(times.index(time)))
            break
    else:
        sys.stdout.write(str(n))

if __name__ == '__main__':
    main()
