n = int(input())
ans = []
for i in range(n):
    ans.append(input())
score = 0
for i in range(n):
    if ans[i] == ans[n-1]:
        score += 1
print(score)
