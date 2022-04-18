
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print('YES' if b-a == c-b else 'NO')

if __name__ == '__main__':
    main()
