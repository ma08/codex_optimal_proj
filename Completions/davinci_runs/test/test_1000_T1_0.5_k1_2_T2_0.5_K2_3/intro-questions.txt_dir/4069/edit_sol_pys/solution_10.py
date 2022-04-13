import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) >= k * d:
        print(abs(x) - k * d)
        exit()
    x = abs(x)
    k -= x // d
    x %= d
    if k % 2 == 0:
        print(x)
        exit()
    print(min(x, d - x))

if __name__ == '__main__':
    main()
