

S = input()
T = input()

for i in range(len(S) - len(T) + 1):
    if T == S[i:i + len(T)]:
        print(len(S) - len(T))
        exit()

print(len(S))