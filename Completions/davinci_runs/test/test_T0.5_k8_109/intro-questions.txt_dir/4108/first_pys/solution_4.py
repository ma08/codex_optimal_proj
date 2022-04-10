

S = input()
T = input()

if len(S) != len(T):
    print("No")
    exit()

if S == T:
    print("Yes")
    exit()

# 各文字の出現回数を数える
S_dict = {}
T_dict = {}
for i in range(len(S)):
    if S[i] in S_dict.keys():
        S_dict[S[i]] += 1
    else:
        S_dict[S[i]] = 1
    if T[i] in T_dict.keys():
        T_dict[T[i]] += 1
    else:
        T_dict[T[i]] = 1

# 出現回数が異なる文字があれば不可能
if S_dict != T_dict:
    print("No")
    exit()

# 各文字の出現回数が同じであれば、2つの文字列が同じ文字を持たないか確認する
S_list = list(S_dict.keys())
for i in range(len(S_list)):
    for j in range(i+1, len(S_list)):
        if S_list[i] in T and S_list[j] in T:
            print("Yes")
            exit()

print("No")