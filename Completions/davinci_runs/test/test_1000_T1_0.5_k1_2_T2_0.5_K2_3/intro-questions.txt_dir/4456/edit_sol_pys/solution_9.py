
def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p = [i - 1 for i in p]
    q = [i - 1 for i in q]
    s = [None] * n
    for i in range(n):
        if s[p[i]] is None:
            s[p[i]] = chr(ord("a") + i)
        if s[q[i]] is None:
            s[q[i]] = s[p[i]]
    for i in range(n):
        if s[i] is None:
            s[i] = s[p[i - 1]]
    print("YES")
    print("".join(s))

main()
