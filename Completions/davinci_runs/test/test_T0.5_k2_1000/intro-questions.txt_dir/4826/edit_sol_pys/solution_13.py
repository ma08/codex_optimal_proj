
import sys

def who_wins(n, m):
    if n % 2 == 1:
        return "A"
    else:
        return "B"

def main():
    n, m = [int(x) for x in sys.stdin.readline().strip().split()]
    print(who_wins(n, m))

if __name__ == '__main__':
    main()
