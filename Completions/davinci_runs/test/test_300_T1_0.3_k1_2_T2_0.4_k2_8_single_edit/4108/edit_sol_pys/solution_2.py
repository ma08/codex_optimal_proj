
s = input()
t = input()

s_counter = {}
t_counter = {}
for i in s:
    if i in s_counter:
        s_counter[i] += 1
    else:
        s_counter[i] = 1
for i in t:
    if i in t_counter:
        t_counter[i] += 1
    else:
        t_counter[i] = 1

if s_counter.items() == t_counter.items():
    print("Yes")
else:
    print("No")
