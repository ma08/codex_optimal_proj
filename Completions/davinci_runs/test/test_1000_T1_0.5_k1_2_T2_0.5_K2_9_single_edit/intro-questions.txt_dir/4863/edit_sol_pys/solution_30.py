n = int(input())
a = [input() for i in range(n)]
score = 0
for i in range(n):
    if a[i] == 'A':  # == is for comparing
        score += 1
print(score)
