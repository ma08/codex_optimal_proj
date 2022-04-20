

# https://www.hackerrank.com/challenges/game-of-thrones/problem

N = int(input())

words = []
for i in range(N):
    words.append(input())

count = 0

for i in range(N):
    word_i = words[i]
    word_j = word_i[::-1]
    for j in range(i+1, N):
        if words[j] == word_j:
            count += 1

print(count)
