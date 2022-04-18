
n = int(input())
answers = [input() for i in range(n)]

score = 0
for i in range(n):
    if i+1 < n:
        if answers[i] == answers[i+1]:
            score += 1

print(score)
