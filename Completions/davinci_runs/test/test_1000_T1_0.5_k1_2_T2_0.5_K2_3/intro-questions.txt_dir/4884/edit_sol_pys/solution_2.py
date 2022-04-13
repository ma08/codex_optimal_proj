
import sys

def main():
    carots = 0
    n, p = map(int, sys.stdin.readline().split())
    for i in range(n):
        sys.stdin.readline()
        carots += p
    print(carots)

if __name__ == '__main__':
    main()
