
import math
#-----main-----

S = input()

# even and odd count
e_cnt = 0
o_cnt = 0

# count even and odd
for i in S:
    if int(i) % 2 == 0:
        e_cnt += 1
    else:
        o_cnt += 1

# output
print(min(e_cnt, o_cnt))
