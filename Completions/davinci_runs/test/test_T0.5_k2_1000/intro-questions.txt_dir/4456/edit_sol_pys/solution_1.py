
def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p = [i - 1 for i in p[:k]]
    q = [i - 1 for i in q[:k]]
    s = [None for i in range(n)]
    for i in range(k - 1):
        s[p[i]] = chr(ord("a") + i + 1)
        s[q[i]] = chr(ord("a") + i + 1)
    for i in range(k - 1, n):
        s[p[i]] = s[q[i]] = s[p[i - 1]] if s[p[i - 1]] is not None else s[q[i - 1]]
    print("YES")
    print("".join(s))

main()
