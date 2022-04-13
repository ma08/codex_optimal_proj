import sys

def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    t = int(input())

    print('Y' if abs(a - c) + abs(b - d) <= t and (abs(a - c) + abs(b - d)) % 2 == t % 2 else 'N')

if __name__ == '__main__':
    main()
