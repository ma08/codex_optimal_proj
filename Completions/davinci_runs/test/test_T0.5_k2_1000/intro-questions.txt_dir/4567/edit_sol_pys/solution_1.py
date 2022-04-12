
# Get input
n = int(input())
s = [int(input()) for i in range(n)]

# Calculate the maximum score that is not a multiple of 10.
max_score = 0
for i in range(n):
    for j in range(i+1, n):
        score = sum(s[i:j])
        if score % 10 != 0 and score > max_score:
            max_score = score

print(max_score)
