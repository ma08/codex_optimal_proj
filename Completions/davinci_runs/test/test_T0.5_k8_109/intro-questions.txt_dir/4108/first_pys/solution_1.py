

S = input()
T = input()

S_set = set(S)
T_set = set(T)

if len(S_set) == len(T_set):
    print('Yes')
else:
    print('No')