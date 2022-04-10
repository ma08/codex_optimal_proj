

# N: number of players, K: points each player starts with, Q: total number of correct answers
N, K, Q = map(int, input().split())

# A: the player who answered correctly
A = []
for i in range(Q):
    a = int(input())
    A.append(a)

# each player's score
score = [K] * N

# each player's survival status
survived = ["No"] * N

for a in A:
    # score of each player except the one who answered correctly
    score[a-1] += 1
    for i in range(N):
        if i != a-1:
            score[i] -= 1
            if score[i] <= 0:
                survived[i] = "Yes"

for s in survived:
    print(s)