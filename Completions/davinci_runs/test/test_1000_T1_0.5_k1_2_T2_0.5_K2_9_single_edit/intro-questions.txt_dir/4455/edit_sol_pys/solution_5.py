
import collections
import sys

def main():
    
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    pairs = collections.defaultdict(set)
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        pairs[a-1].add(b-1)
        pairs[b-1].add(a-1)

    ans = [0]*n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if j in pairs[i]:
                continue
            if arr[i] > arr[j]:
                ans[i] += 1
    
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()
