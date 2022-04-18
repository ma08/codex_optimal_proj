n = int(input())
a = [input() for i in range(n)]
score = 0
for i in range(n):
    if a[i] == 'A' or a[i] == 'A+':
        score += 1
    elif a[i] == 'A-':
        score += 0.9
    elif a[i] == 'B+':
        score += 0.8
    elif a[i] == 'B':
        score += 0.7
    elif a[i] == 'B-':
        score += 0.6
    elif a[i] == 'C+':
        score += 0.5
    elif a[i] == 'C':
        score += 0.4
    elif a[i] == 'D':
        score += 0.3
    elif a[i] == 'F':
        score += 0.0
    else:
        score += 0.0
print(score)
