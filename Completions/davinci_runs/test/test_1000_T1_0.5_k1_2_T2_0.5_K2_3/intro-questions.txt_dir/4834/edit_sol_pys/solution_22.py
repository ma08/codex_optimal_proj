import sys

def main():
    n = int(sys.stdin.readline())
    times = [int(x) for x in sys.stdin.readline().split()] * 2
    times.sort()

    a = 0
    b = 0
    for i in range(n * 2):
        if i < n:
            if i % 2 == 0:
                a += times[i]
            else:
                b += times[i]
        elif i > n:
            if i % 2 == 0:
                b += times[i]
            else:
                a += times[i]

    print(max(a, b))

if __name__ == '__main__':
    main()
