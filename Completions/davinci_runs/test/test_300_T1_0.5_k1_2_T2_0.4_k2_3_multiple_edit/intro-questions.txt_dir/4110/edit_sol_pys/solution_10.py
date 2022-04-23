import sys
sys.setrecursionlimit(10**6)

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    def dfs(i, m, s):
        nonlocal ans
        if m == 0:
            ans = max(ans, s)
            return
        if i >= N:
            return
        dfs(i+1, m, s)
        dfs(i+1, m-1, s+A[i])
    dfs(0, M, 0)
    print(ans)
    
    # calculate the minimum number of problems that need to be solved
    # in order to have a total score of G or more points
    ans = float('inf')
    for i in range(2**D):
        score = 0
        res = 0
        for j in range(D):
            if (i>>j)&1:
                score += 100 * (j+1) * p[j] + c[j]
                res += p[j]
        for j in range(D-1, -1, -1):
            if (i>>j)&1 == 0:
                for k in range(p[j]):
                    res += 1
                    score += 100 * (j+1)
                    if score >= G:
                        break
                break
        if score >= G:
            ans = min(ans, res)
    print(ans)

if __name__ == "__main__":
    main()
