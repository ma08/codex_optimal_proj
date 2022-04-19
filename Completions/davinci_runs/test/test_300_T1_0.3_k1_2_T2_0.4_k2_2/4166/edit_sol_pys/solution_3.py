import sys
sys.setrecursionlimit(10**6)


def dfs(s, i):
    if i == N:
        return int(s)

    if s[i] != '?':
        return dfs(s, i+1)

    for j in range(10):
        s_next = s[:i] + str(j) + s[i+1:]
        ans = dfs(s_next, i+1)
        if ans is not None:
            return ans

    return None


def main():
    s = input()
    ans = dfs(s, 0)
    print(ans)


if __name__ == '__main__':
    main()


N, M = map(int, input().split())

s = []
c = []
for _ in range(M):
    s_i, c_i = map(int, input().split())
    s.append(s_i)
    c.append(c_i)

ans = -1
for i in range(10**N):
    i_str = str(i)
    if len(i_str) != N:
        continue
    for j in range(M):
        if i_str[s[j]-1] != str(c[j]):
            break
    else:
        ans = i
        break

print(ans)
