
n = int(input())
answers = [input() for i in range(n)]

score = 0
for i in range(n):
    if i + 1 < n:
        score += answers[i] == answers[i + 1]

print(score)
