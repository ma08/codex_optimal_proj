
import sys

def input():
    return sys.stdin.readline().strip()

def main():
    A, B = map(int, input().split())
    print(A + B)

if __name__ == '__main__':
    main()
