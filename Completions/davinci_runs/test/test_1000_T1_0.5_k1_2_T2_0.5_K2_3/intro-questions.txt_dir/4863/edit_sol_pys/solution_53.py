

n = int(input())
ans = input().split()
ans = [ans[i] for i in range(len(ans)) if i != n-1 and ans[i] != ""]

print(len(ans))
