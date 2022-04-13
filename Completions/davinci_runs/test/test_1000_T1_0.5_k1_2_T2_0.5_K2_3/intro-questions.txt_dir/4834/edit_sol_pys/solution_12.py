import sys

def main():
    n = int(sys.stdin.readline())
    times = [int(x) for x in sys.stdin.readline().split()]

    times.sort()

    total = 0
    for i in range(n):
        total += (n - i) * times[i]

    sys.stdout.write(str(total) + "\n")


if __name__ == '__main__':
    main()
