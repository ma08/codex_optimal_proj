
S = input()
T = input()
answer = 0
for i in range(3):
    if S[i] == T[i]:
        answer += 1
print(answer)
