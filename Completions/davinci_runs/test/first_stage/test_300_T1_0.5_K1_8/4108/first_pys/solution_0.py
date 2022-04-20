

N = int(input())
S = input()
T = input()

S_set = set(S)
T_set = set(T)
S_dict = {}
T_dict = {}

for s in S_set:
    S_dict[s] = S.count(s)
for t in T_set:
    T_dict[t] = T.count(t)

if sorted(S_dict.items()) == sorted(T_dict.items()):
    print('Yes')
else:
    print('No')