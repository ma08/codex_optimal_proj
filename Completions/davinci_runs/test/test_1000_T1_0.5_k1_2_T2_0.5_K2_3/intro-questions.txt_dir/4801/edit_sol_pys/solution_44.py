# https://codeforces.com/contest/1144/problem/A


n = int(input())
a = list(map(int, input().split()))  # read a list of integers, 2 in this case

g = [0] * n  # create a list of zeros
g[0] = a[0]

for i in range(1, n):
    if a[i] >= g[-1]:
        g.append(a[i])
    else:
        for j in range(len(g)):
            if a[i] <= g[j]:
                g[j] = a[i]
                break

print(len(g))
print(*g)
