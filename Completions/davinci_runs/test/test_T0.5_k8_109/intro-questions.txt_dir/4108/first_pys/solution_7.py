

S = input()
T = input()

if len(set(S)) != len(set(T)):
    print("No")
    exit()

d = {}
for s, t in zip(S, T):
    if s in d:
        if d[s] != t:
            print("No")
            exit()
    else:
        d[s] = t

print("Yes")