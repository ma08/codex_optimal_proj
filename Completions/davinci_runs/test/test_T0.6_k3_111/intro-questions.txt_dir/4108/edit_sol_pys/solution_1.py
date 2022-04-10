
s = input()
t = input()

# 各文字が出現する回数を数える。
s_dict = {}
t_dict = {}

for s_i in s:
    if s_dict.get(s_i) is None:
        s_dict[s_i] = 0
    s_dict[s_i] += 1

for t_i in t:
    if t_dict.get(t_i) is None:
        t_dict[t_i] = 0
    t_dict[t_i] += 1

# 各文字の出現回数が等しいかチェック。
for k in s_dict.keys():
    if t_dict.get(k) is None or s_dict[k] != t_dict[k]:
        print("No")
        exit()

print("Yes")
