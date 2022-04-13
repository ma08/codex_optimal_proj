

from sys import stdin

def solve(n, k, x, a):
    if x < k:
        return -1
    elif k == 1:
        return sum(a)
    else:
        prefix = [0] + a[:n-k+1]
        suffix = a[k-1:] + [0]
        max_suffix = [0]
        for i in range(n-k, -1, -1):
            max_suffix.append(max(max_suffix[-1], suffix[i]))
        max_suffix = max_suffix[::-1]
        res = 0
        for i in range(n-k+1):
            res = max(res, prefix[i]+max_suffix[i+1])
        return res

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))
 
if __name__ == "__main__":
    main()
