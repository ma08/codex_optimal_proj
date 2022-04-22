
import sys
sys.setrecursionlimit(10**7)


def dfs(i, n, s, c, min_num, max_num):
    if i == n:
        if min_num <= int(''.join(s)) <= max_num:
            print(int(''.join(s)))
            exit()
        else:
            return

    if c[i] != -1:
        s[i] = str(c[i])
        dfs(i+1, n, s, c, min_num, max_num)
    else:
        if i == 0:
            s[i] = str(1)
            dfs(i+1, n, s, c, min_num, max_num)
            s[i] = str(0)
            dfs(i+1, n, s, c, min_num, max_num)
        else:
            s[i] = str(0)
            dfs(i+1, n, s, c, min_num, max_num)
            s[i] = str(9)
            dfs(i+1, n, s, c, min_num, max_num)


def solve():
    n, m = map(int, input().split())
    s = [-1] * n
    c = [-1] * n
    for i in range(m):
        tmp = list(map(int, input().split()))
        s[tmp[0]-1] = tmp[1]
        c[tmp[0]-1] = tmp[1]

    min_num = 0
    max_num = 10**n - 1
    dfs(0, n, s, c, min_num, max_num)
    print(-1)


if __name__ == '__main__':
    solve()


"""

N, M = map(int, input().split())

s = []
c = []

for i in range(M):
    tmp = list(map(int, input().split()))
    s.append(tmp[0])
    c.append(tmp[1])

min_num = 0
max_num = 10**N

for i in range(min_num, max_num):
    num_str = str(i)
    if len(num_str) != N:
        continue
    is_match = True
    for j in range(M):
        if int(num_str[s[j]-1]) != c[j]:
            is_match = False
            break
    if is_match:
        print(i)
        exit()

print(-1)
"""
