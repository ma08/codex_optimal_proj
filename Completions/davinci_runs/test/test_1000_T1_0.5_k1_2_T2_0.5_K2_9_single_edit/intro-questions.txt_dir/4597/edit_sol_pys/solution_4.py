
import sys


def main():
    n, k = [int(i) for i in sys.stdin.readline().split()]

    ans = 0
    for i in range(k, n+2):
        ans += (n-i+1) * i + 1

    print(ans)

if __name__ == '__main__':
    main()
