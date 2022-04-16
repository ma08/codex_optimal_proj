
import sys

def main():
    n = int(input())
    temps = list(map(int, input().split()))
    temps.sort()
    if n % 2 == 0:
        for i in range(0, n, 2):
            print(temps[i], end=' ')
        for i in range(n - 1, 0, -2):
            print(temps[i], end=' ')
    else:
        for i in range(0, n, 2):
            print(temps[i], end=' ')
        for i in range(n - 2, 0, -2):
            print(temps[i], end=' ')
        print(temps[-1], end=' ')

if __name__ == '__main__':
    main()
