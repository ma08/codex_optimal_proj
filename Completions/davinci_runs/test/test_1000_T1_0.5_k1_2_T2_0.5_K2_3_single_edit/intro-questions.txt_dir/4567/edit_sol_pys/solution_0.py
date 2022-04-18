
import sys

def main():
    a, b, c, k = map(int, sys.stdin.readline().rstrip().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    elif a + b + c >= k:
        print(a - (k - a - b))

if __name__ == '__main__':
    main()
