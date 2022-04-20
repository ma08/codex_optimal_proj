
import sys


def main():
    k = int(input())
    x = 7
    i = 1
    while True:
        if x % k == 0:
            print(i)
            return
        x = x * 10 + 7
        i += 1

if __name__ == '__main__':
    main()
