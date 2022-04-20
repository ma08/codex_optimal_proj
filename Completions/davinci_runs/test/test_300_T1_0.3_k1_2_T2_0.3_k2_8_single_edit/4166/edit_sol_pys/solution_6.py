import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

def rec(i, s, c):
    if i == M:
        return ''.join(s)
    if s[c[i][0]-1] == str(c[i][1]):
        return ''.join(s)
    if s[c[i][0]-1] == '-':
        s[c[i][0]-1] = str(c[i][1])
        return ''.join(rec(i+1, s, c))
    else:
        s[c[i][0]-1] = str(c[i][1])
        return ''.join(rec(i+1, s, c))

def main():
    s = ['-' for i in range(N)]
    c = []
    for i in range(M):
        c.append(list(map(int, input().split())))
    ans = ''.join(rec(0, s, c))
    if '-' in ans or ans == '':
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()
