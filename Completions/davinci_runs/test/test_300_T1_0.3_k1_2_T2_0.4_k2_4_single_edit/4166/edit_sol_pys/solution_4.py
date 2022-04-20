import sys


N, M = map(int, sys.stdin.readline().split())

def rec(i, s, c):
    if i == M:
        return s
    if s[c[i][0]-1] == str(c[i][1]):
        return s
    if s[c[i][0]-1] == '-':
        s[c[i][0]-1] = str(c[i][1])
        return rec(i+1, s, c)
    else:
        s[c[i][0]-1] = str(c[i][1])
        return rec(i+1, s, c)

def main():
    s = ['-' for i in range(N)]
    c = []
    for i in range(M):
        c.append(list(map(int, sys.stdin.readline().split())))
    ans = rec(0, s, c)
    if '-' in ans:
        print(-1)
    else:
        print(''.join(ans))

if __name__ == '__main__':
    main()
