

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p = [i - 1 for i in p]
    q = [i - 1 for i in q]
    s = ["" for i in range(n)]
    for i in range(k):
        s[p[i]] = chr(ord("a") + i)
        s[q[i]] = chr(ord("a") + i)
    for i in range(k, n):
        s[p[i]] = s[q[i]] = s[p[i - k]]
    print("YES")
    print("".join(s))

main()
