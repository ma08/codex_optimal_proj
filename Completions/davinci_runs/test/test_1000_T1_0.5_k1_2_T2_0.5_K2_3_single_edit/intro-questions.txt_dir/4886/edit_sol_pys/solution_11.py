
import sys


def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    if k >= n:
        print("Your wish is granted!")
    else:
        print("You will become a flying monkey!")


if __name__ == '__main__':
    main()
