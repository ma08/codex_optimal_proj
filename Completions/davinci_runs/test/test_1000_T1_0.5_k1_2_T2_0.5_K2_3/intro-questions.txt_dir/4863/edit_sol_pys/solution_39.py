n = int(input())
answers = [input()]
for i in range(n):
    if answers[-1] == input():
        answers.append(answers[-1])
    else:
        answers.append(input())

score = 0
for i in range(len(answers) - 1):
    if answers[i] == answers[i + 1]:
        score += 1

print(score)
