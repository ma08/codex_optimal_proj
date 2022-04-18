

    import sys
    sys.setrecursionlimit(10 ** 6)
def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # q = list(map(int, input().split()))
    p = [i - 1 for i in p]
    # q = [i - 1 for i in q]
    s = [None for i in range(n)]
    for i in range(k):
        s[p[i]] = chr(ord("a") + i)  # a, b, c, ...
    for i in range(k, n):
        s[p[i]] = s[q[i]] = s[p[i - 1]]
    print("Yes")
    print("".join(s))

main()
