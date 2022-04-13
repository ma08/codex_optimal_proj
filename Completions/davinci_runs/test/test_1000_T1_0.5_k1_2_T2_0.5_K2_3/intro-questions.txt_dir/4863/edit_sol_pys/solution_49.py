n = int(input())
a = [input() for _ in range(n)]
score = 0
for _ in range(n):
    if a[_] == 'A':
        score += 1
print(score)
