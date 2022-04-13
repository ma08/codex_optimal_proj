
n = int(input())
ans = []
for i in range(n):
    ans.append(input())
score = 0
for i in range(n):
    if i == n-1:
        score += 1
    elif ans[i] == ans[i+1]:
        score += 1
print(score)
