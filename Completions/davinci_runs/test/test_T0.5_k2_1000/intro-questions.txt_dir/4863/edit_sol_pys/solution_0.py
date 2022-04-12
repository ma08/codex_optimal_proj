
n = int(input())
a = [int(input()) for i in range(n)]
score = 0
for i in range(n):
    if a[i] == 1:
        score += 1
print(score)
