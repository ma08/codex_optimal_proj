

N = int(input())
S = input()

count = 0
for i in range(N):
    if S[i] == 'A':
        for j in range(i + 1, N):
            if S[j] == 'B':
                for k in range(j + 1, N):
                    if S[k] == 'C':
                        count += 1

print(count)