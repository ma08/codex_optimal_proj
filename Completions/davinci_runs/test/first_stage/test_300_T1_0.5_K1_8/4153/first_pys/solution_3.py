

N = int(input())
S = list(input())

count = 0

for i in range(1, N):
    if S[i-1] != S[i]:
        count += 1

print(count)