

S = input()
T = input()

if len(S) != len(T):
    print("No")
    exit()

dic = {}
for s, t in zip(S, T):
    if s not in dic:
        if t not in dic.values():
            dic[s] = t
        else:
            print("No")
            exit()
    else:
        if dic[s] != t:
            print("No")
            exit()

print("Yes")