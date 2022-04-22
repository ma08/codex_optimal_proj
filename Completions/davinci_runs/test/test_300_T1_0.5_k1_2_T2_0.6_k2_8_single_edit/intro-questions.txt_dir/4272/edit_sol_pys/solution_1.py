
n, m = map(int, input().split())
s = [input() for _ in range(n)]
t = [input() for _ in range(m)]
for i in range(n - m + 1):
    for j in range(n - m + 1):
        for k in range(m):
            if s[i + k][j:j + m] != t[k]:
                break
        else:
            print("Yes")
            exit()
print("No")
