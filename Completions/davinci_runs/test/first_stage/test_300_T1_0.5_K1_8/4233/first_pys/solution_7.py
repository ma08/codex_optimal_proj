

def main():
    n,m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input())
    ans = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                l = 0
                while j + l < m and a[i][j + l] == '*':
                    l += 1
                r = 0
                while j - r >= 0 and a[i][j - r] == '*':
                    r += 1
                u = 0
                while i - u >= 0 and a[i - u][j] == '*':
                    u += 1
                d = 0
                while i + d < n and a[i + d][j] == '*':
                    d += 1
                if l != r or u != d or l != u or r != d:
                    print(-1)
                    return
                for g in range(1,l):
                    for h in range(1,l):
                        if a[i + h][j + g] != '*':
                            print(-1)
                            return
                ans.append([i + 1,j + 1,l])
    print(len(ans))
    for i in range(len(ans)):
        print(*ans[i])

main()