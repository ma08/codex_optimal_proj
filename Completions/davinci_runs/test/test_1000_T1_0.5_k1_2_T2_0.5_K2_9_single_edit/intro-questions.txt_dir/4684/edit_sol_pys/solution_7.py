import sys
input = sys.stdin.readline

def main():
    r, g, b = map(int, input().rstrip().split())
    num = r * 100 + g * 10 + b
    if num % 4 == 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
