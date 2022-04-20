
import sys

def main():
    """
    main
    """
    k = int(sys.stdin.readline().rstrip())
    x = int(sys.stdin.readline().rstrip())

    for i in range(x - k + 1, x + k):
        print(i, end=' ')

if __name__ == '__main__':
    main()