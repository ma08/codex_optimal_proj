
import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]
    if h <= n:
        print(0)
    elif h <= m:
        print(1)
    elif h <= n+m:
        print(2)
    else: # h > n+m
        print(h-n-m)

if __name__ == '__main__':
    main()
