
S = input() #input string
count = 0

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        count += 1

print(count)
