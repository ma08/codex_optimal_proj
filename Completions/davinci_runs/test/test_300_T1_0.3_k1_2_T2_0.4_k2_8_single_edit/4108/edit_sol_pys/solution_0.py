

import collections

s = input()
t = input()

s_counter = collections.Counter(s)
t_counter = collections.Counter(t)

if s_counter == t_counter:
    print("Yes")
else:
    print("No")
