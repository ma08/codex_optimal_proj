

import sys

def main():
    n = int(input())
    temperatures = list(map(int, input().split()))  # Вводим массив
    temperatures.sort()
    if n % 2 == 0:  # Если число элементов четное
        for i in range(0, n, 2):
            print(temperatures[i], end=' ')
        for i in range(n - 1, 0, -2):
            print(temperatures[i], end=' ')
    else:  # Если нечетное
        for i in range(0, n, 2):
            print(temperatures[i], end=' ')
        for i in range(n - 2, 0, -2):
            print(temperatures[i], end=' ')
        print(temperatures[-1], end=' ')

if __name__ == '__main__':
    main()
