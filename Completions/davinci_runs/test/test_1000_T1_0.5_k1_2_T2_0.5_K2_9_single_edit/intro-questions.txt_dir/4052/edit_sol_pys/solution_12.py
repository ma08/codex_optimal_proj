

def main():
    # read data for n sequences
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # solve
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            if s[i] == t[j]:
                tmp += 1
        ans = max(ans, tmp)

    print(ans)

main()
