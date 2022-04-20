
import sys

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if d == 1 or n <= d * k:
        print('YES\n' + '\n'.join(f'{i} {i + 1}' for i in range(1, n)))
    else:
        print('NO')

if __name__ == '__main__':
    main()
