
n = int(input())
ans = list(map(int, input().split()))

ans = [ans[i] for i in range(len(ans)) if i != n-1]

print(*ans)
