

import sys

def main():
    n = int(sys.stdin.readline())
    times = [int(x) for x in sys.stdin.readline().split()][:n]
    times.sort()

    a = 0
    b = 0
    for i in range(n//2):
        if i % 2 == 0:
            a += times[2*i] + times[2*i+1]
        else:
            b += times[2*i] + times[2*i+1]

    if n % 2 != 0:
        a += times[n-1]

    print(max(a, b))

if __name__ == '__main__':
    main()
