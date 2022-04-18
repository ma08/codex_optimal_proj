

def solve(n, m, k):
    if k > n or k > m:
        return -1
    if k == 1:
        return n*m
    if k == n or k == m:
        return max(n, m)
    if n > m:
        return m*(k-1) + (n-k+1)
    else:
        return n*(k-1) + (m-k+1)

def main():
    n, m, k = map(int, input().split())
    print(solve(n, m, k))

if __name__ == "__main__":
    main()
