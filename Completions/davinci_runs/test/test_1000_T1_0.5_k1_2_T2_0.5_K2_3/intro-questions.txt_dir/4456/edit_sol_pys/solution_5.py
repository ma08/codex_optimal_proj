

def dfs(i, s):
    if i == k:
        return True
    if p[i] in s or q[i] in s:
        return False
    s.add(p[i])
    s.add(q[i])
    return dfs(i + 1, s)

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p = [i - 1 for i in p]
    q = [i - 1 for i in q]
    s = [None] * n
    for i in range(k):
        s[p[i]] = chr(ord("a") + i)
        s[q[i]] = chr(ord("a") + i)
    for i in range(k, n):
        s[p[i]] = s[q[i]] = s[p[i - 1]]
    print("YES")
    print("".join(s))

main()
