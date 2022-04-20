

n, m = map(int, input().split())
s = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    s[i] = list(map(int, input().split()))

for i in range(10**(n-1), 10**n):
    num = list(str(i))
    for j in range(m):
        if num[s[j][0]-1] != str(s[j][1]):
            break
    else:
        print(i)
        exit()

print(-1)