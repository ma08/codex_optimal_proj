import sys

def main():
    x, k, d = map(int, sys.stdin.readline().split())
    if x < 0:
        x = -x
    if x < k * d:
        x = x % d
        if x > d - x:
            x = d - x
    print(x)

if __name__ == '__main__':
    main()
