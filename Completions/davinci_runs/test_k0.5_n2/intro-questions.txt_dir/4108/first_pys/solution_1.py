

S = input()
T = input()

S_list = list(S)
T_list = list(T)

S_list.sort()
T_list.sort()

if S_list == T_list:
    print('Yes')
else:
    print('No')