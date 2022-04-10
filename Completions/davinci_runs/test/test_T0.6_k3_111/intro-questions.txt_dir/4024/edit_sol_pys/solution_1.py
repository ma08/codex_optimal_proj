import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    print(subsequence(s, n, k))


    if k == 1:
        return 0
def subsequence(s, n, k):
    if k == n:
        return 0
    elif k > n:
        return -1

    for i in range(n):
        cost = i + subsequence(s[i:], n - i, k - 1)
        if cost >= 0 and cost < n:
            return cost + 1
    return -1


if __name__ == '__main__':
    main()
