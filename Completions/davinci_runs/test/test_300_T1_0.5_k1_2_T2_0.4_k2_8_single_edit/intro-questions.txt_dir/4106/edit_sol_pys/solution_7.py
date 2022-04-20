
from sys import stdin
from itertools import accumulate

def solve(n, k, x, a):
    return -1 if x < k else sum(a) if k == 1 else max(sum(a[i:i+k]) for i in range(n-k+1))

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()
