

import sys


def main():
    line = sys.stdin.readline().rstrip()
    N, K = line.split(' ')
    N, K = int(N), int(K)
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                if (a + b) % K == 0 and (b + c) % K == 0 and (c + a) % K == 0:
                    ans += 1
    print(ans)


if __name__ == '__main__':
    main()
