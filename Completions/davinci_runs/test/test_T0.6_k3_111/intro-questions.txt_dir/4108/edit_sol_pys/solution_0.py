s = input()
t = input()

# s = "azazel"
# t = "apple"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "bcdefghijklmnopqrstuvwxyza"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "bcdefghijklmnopqrstuvwxyz"

s_dict = {}
s_list = list(s)
for i in s_list:
    if i in s_dict:
        s_dict[i] += 1
    else:
        s_dict[i] = 1

t_dict = {}
t_list = list(t)
for i in t_list:
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


s = input()
t = input()

# s = "azazel"
# t = "apple"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "bcdefghijklmnopqrstuvwxyza"

# s = "abcdefghijklmnopqrstuvwxyz"
# t = "bcdefghijklmnopqrstuvwxyz"

s_dict = {}
s_list = list(s)
for i in s_list:
    if i in s_dict:
        s_dict[i] += 1
    else:
        s_dict[i] = 1

t_dict = {}
t_list = list(t)
for i in t_list:
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
