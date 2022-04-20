N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]


A.sort(reverse=True)

AB.sort(key=lambda x: x[0])

ans = 0
for i in range(N):
    if M > AB[i][1]:
        ans += AB[i][0] * AB[i][1]
        M -= AB[i][1]
    else:
        ans += AB[i][0] * M
        break

print(ans)
