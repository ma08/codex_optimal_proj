
import sys

def main():
    d, n = map(int, input().split())
    if d == 0:
        print(n * 1)
    elif d == 1:
        print(n * 100)
    else:
        print(n * 10000)

if __name__ == '__main__':
    main()
