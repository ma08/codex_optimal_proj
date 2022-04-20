

N = int(input())
S = input()

count = 0
for i in range(0, N - 2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        count += 1

print(count)