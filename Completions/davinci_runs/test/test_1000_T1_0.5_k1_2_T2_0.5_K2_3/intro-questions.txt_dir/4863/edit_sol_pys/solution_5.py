
n = int(input())
answers = []
for i in range(n):
    answers.append(input())

score = 0
for i in range(n):
    if i+1 < n and answers[i] == answers[i+1]:
        score += 1

print(score)
