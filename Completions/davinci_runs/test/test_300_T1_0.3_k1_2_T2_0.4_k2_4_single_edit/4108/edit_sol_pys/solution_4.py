# coding: utf-8

s = input()
t = input()

if len(s) != len(t):
    print("No")
    exit()

s_list = list(s)
t_list = list(t)

s_list.sort()
t_list.sort()

if s_list == t_list:
    print("Yes")
else:
    print("No")
