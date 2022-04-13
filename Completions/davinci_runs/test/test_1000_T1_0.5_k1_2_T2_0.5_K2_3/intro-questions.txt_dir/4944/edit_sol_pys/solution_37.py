n, q = map(int, input().split())
s = input()
lr = []
for i in range(q):
    lr.append(list(map(int, input().split())))
ans = 0
for i in range(q):
    ans = 0
    for j in range(lr[i][0]-1, lr[i][1]-1):
        if s[j] == 'A' and s[j+1] == 'C':
            ans += 1
    print(ans)
