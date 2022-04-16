

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    s = [None for i in range(n)]
    for i in range(k):
        s[p[i] - 1] = chr(ord("a") + i)
        s[q[i] - 1] = chr(ord("a") + i)
    for i in range(k, n):
        s[p[i] - 1] = s[q[i] - 1] = s[p[i - 1] - 1]
    print("YES")
    print("".join(s))

main()
