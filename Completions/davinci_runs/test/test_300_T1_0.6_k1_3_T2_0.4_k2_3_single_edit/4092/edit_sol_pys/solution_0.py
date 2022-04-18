
import sys

sys.setrecursionlimit(10**6)

def dfs(i, v, d):
    if i == n+1:
        return 0
    if (i, v) in d:
        return d[(i, v)]
    ret = dfs(i+1, v, d)
    if v[i] == '.':
        ret = max(ret, dfs(i+1, v[:i] + 'o' + v[i+1:], d) + 1)
    d[(i, v)] = ret
    return ret

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.append(0)
    a.insert(0, 0)
    s = [0] * (n+2)
    for i in range(1, n+2):
        s[i] = s[i-1] + a[i]
    d = {}
    ans = 0
    for i in range(n+1):
        if s[i] not in d:
            d[s[i]] = i
        else:
            ans = max(ans, i - d[s[i]] - 1)
    print(ans)
    
if __name__ == "__main__":
    main()
