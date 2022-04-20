
N, M = map(int, input().split())


def rec(i, s, c, ans):
    if i == M:
        ans.append(s)
        return
    if s[c[i][0] - 1] == str(c[i][1]):
        rec(i + 1, s, c, ans)
    elif s[c[i][0] - 1] == '-':
        s[c[i][0] - 1] = str(c[i][1])
        rec(i + 1, s, c, ans)
    else:
        s[c[i][0] - 1] = str(c[i][1])
        rec(i + 1, s, c, ans)


def main():
    s = ['-' for i in range(N)]
    c = []
    for i in range(M):
        c.append(list(map(int, input().split())))
    ans = []
    rec(0, s, c, ans)
    if len(ans) == 0:
        print(-1)
    else:
        print(''.join(ans))

if __name__ == '__main__':
    main()
