
import sys

def main():
    n, a, b = [int(x) for x in sys.stdin.readline().split()]

    if b / n > a:
        print(a * n, end='')
    else:
        print(b, end='')

if __name__ == '__main__':
    main()
