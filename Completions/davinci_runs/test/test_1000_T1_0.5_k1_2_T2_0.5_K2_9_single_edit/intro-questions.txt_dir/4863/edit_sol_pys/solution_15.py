

n = int(input())
a = [input() for i in range(n)]
score = 0
for i in range(n):
    if a[i] == 'A' or a[i] == 'C' or a[i] == 'G' or a[i] == 'T':
        score += 1
print(score)
