import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

def rec(i, s):
    if i == N:
        if s[i-1] == '-':
            return False
        else:
            for j in range(M):
                if s[c[j][0]-1] != str(c[j][1]):
                    return False
            return True
    for j in range(10):
        if s[i-1] == '-' or s[i-1] == str(j):
            s[i-1] = str(j)
            if rec(i+1, s):
                return True
            s[i-1] = '-'
    return False

def main():
    s = ['-' for i in range(N)]
    c = []
    for i in range(M):
        c.append(list(map(int, input().split())))
    if rec(1, s):
        print(''.join(s))
    else:
        print(-1)
    else:
        print(''.join(ans))

if __name__ == '__main__':
    main()
