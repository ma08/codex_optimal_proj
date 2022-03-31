
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    if k == 1:
        print(0)
    else:
        print(subsequence(s, n, k))


def subsequence(s, n, k):
    if k == n:
        return 0
    elif k > n:
        return -1

    cost = 0
    for i in range(1, n):
        cost += i
        if k == 2:
            return cost
        cost += subsequence(s[i:], n-i, k-1)
        if cost >= 0:
            return cost
    return -1


if __name__ == '__main__':
    main()