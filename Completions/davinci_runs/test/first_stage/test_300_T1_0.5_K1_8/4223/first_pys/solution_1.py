

N = int(input())
S = input()

c = S[0]
count = 1

for i in range(1, N):
    if c != S[i]:
        c = S[i]
        count += 1

print(count)