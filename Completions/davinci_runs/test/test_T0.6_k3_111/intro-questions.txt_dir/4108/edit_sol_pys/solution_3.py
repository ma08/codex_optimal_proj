
s = input()
t = input()

s_dict = {}
for i in s:
    if i in s_dict:
        s_dict[i] += 1
    else:
        s_dict[i] = 1

t_dict = {}
for i in t:
    if i in t_dict:
        t_dict[i] += 1
    else:
        t_dict[i] = 1

for k, v in t_dict.items():
    if k not in s_dict:
        print("No")
        exit()
    else:
        if v > s_dict[k]:
            print("No")
            exit()

print("Yes")
