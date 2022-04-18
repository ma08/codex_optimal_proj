import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().strip().split())
    if b-a == c-b and c-b == d-c:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
