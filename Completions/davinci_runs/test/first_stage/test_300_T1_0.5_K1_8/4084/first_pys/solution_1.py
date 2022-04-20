

import sys
readline = sys.stdin.readline


def main():
    N, A, B = map(int, readline().rstrip().split())
    ans = N // (A + B) * A + min(N % (A + B), A)
    print(ans)


if __name__ == '__main__':
    main()