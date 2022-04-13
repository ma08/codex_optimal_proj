n = int(input())
a = [input() for _ in range(n)]
score = 0
for i in range(n):
    if a[i] == "A":
        score += 1
print(score)
