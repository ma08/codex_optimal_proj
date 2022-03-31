import sys

def main():
    n = int(sys.stdin.readline())
    divisors = [int(x) for x in sys.stdin.readline().split()]

    x = 1
    y = 1
    for i in range(n):
        if i < n // 2:
            x *= divisors[i]
        else:
            y *= divisors[i]

    print(x, y)

if __name__ == '__main__':
    main()
