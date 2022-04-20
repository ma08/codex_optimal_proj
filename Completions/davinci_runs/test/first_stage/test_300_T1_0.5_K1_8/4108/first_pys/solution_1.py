

S = input()
T = input()

if len(S) != len(T):
    print("No")
    exit()

s = set(S)
t = set(T)

if len(s) != len(t):
    print("No")
    exit()

if len(s) == 1:
    print("Yes")
    exit()

for i in range(len(S)):
    if S[i] == T[i]:
        continue
    else:
        if S[i] in T[i:]:
            T = T[:i] + T[i:].replace(S[i], T[i])
        elif T[i] in S[i:]:
            S = S[:i] + S[i:].replace(T[i], S[i])
        else:
            print("No")
            exit()

if S == T:
    print("Yes")
else:
    print("No")