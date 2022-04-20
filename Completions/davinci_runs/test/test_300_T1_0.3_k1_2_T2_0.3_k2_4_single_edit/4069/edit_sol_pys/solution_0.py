
import sys

def main():
    x, k, d = map(int, sys.stdin.readline().split())
    if abs(x) < k * d:
        print(abs(x) % d)
    else:
        print(abs(x) - k * d)

if __name__ == '__main__':
    main()
