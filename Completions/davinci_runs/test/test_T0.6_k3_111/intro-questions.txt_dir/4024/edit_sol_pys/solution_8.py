
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(subsequence(s, n, k))


def subsequence(s, n, k):
    if k == 1:
        return -1
    elif k > n or k < 1:
        return -1

    cost = -1
    for i in range(1, n):
        cost += i
        cost = max(cost, subsequence(s[i:], n-i, k-1))
    return cost


if __name__ == '__main__':
    main()
