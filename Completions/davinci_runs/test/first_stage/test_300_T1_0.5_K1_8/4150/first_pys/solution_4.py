

import sys

def main():
    n, k = map(int, sys.stdin.readline().strip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    team = [0] * n
    for i in range(n):
        ai = a[i]
        if team[i] == 0:
            team[i] = 1
            left = max(0, i - k)
            right = min(n - 1, i + k)
            for j in range(left, right + 1):
                if j != i and a[j] < ai:
                    team[j] = 1
    for i in range(n):
        if team[i] == 0:
            team[i] = 2
            left = max(0, i - k)
            right = min(n - 1, i + k)
            for j in range(left, right + 1):
                if j != i and a[j] < ai:
                    team[j] = 2
    print(''.join(map(str, team)))

if __name__ == "__main__":
    main()