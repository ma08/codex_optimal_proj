import sys

def main():
    x, k, d = map(int, sys.stdin.readline().split())
    x = abs(x)
    if x >= k * d:
        print(x - k * d)
    else:
        x = x % d
        if x > d - x:
            print(d - x)
        else:
            print(x)

if __name__ == '__main__':
    main()
