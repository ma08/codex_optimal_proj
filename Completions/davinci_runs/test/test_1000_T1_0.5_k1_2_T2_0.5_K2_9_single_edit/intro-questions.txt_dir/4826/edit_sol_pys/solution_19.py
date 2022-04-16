import sys
input = sys.stdin.readline


def main():
    n = int(input().strip())
    if n % 2 == 1:
        print('Alice')
    else:
        print('Bob')

if __name__ == '__main__':
    main()
