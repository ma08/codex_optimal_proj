
import sys

def main():
    n = int(input())
    temperatures = list(map(int, sys.stdin.read().split()))
    temperatures.sort()
    if n % 2 == 0:
        for i in range(0, n // 2):
            print(temperatures[i], end=' ')  # print the first half of the list
        for i in range(n - 1, n // 2 - 1, -1):
            print(temperatures[i], end=' ')  # print the second half of the list
    else:
        for i in range(0, n, 2):
            print(temperatures[i], end=' ')
        for i in range(n - 2, 0, -2):
            print(temperatures[i], end=' ')
        print(temperatures[-1], end=' ')

if __name__ == '__main__':
    main()
