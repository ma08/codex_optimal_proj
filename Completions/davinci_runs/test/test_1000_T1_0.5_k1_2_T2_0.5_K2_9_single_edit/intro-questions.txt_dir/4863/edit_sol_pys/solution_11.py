

n = int(input())
ans = input().split()

ans = [ans[i] for i in range(len(ans)) if i != n-1 and i != n-2]

print(len(ans))
