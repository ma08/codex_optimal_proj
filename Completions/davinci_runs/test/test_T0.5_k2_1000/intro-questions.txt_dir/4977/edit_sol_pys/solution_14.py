import sys

def main():
    a, b = map(int, input().strip().split())
    c, d = map(int, input().strip().split())
    t = int(input().strip())

    if abs(a - c) + abs(b - d) <= t and (abs(a - c) + abs(b - d)) % 2 == t % 2:
        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    main()
