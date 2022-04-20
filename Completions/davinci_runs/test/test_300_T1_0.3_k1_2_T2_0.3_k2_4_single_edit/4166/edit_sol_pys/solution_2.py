
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

def rec(i, s, c, ans):
    if i == M and '-' not in s:
        ans.append(s)
        return
    for j in range(M):
        if s[c[j][0]-1] == str(c[j][1]):
            continue
        if s[c[j][0]-1] == '-':
            s[c[j][0]-1] = str(c[j][1])
            rec(i+1, s, c, ans)
            s[c[j][0]-1] = '-'
        else:
            s[c[j][0]-1] = str(c[j][1])
            rec(i+1, s, c, ans)
            s[c[j][0]-1] = '-'

def main():
    s = ['-' for i in range(N)]
    c = []
    for i in range(M):
        c.append(list(map(int, input().split())))
    ans = []
    rec(0, s, c, ans)
    if ans == []:
        print(-1)
    else:
        print(''.join(ans[0]))

if __name__ == '__main__':
    main()
