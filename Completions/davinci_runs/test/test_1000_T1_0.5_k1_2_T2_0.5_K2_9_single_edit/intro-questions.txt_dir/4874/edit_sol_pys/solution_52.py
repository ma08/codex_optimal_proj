# https://codeforces.com/contest/1365/problem/A

n, m = map(int, input().split())

dance = []
for _ in range(n):
    dance.append(input())

count = 0
for i in range(m):
    if dance[0][i] == '$':
        count += 1
        while i < m and dance[0][i] == '$':
            i += 1

print(count)
