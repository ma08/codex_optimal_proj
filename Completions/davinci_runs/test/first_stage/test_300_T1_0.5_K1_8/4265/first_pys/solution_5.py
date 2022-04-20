

S = input()
T = input()

operations = 0
for i in range(len(S)):
    if S[i] != T[i]:
        operations += 1
print(operations)