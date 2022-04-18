
#-----main-----

S = input()

# 0, 1 count
zero_cnt = 0
one_cnt = 0

# count 0 and 1
for i in S:
    if i == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

# output
print(min(zero_cnt, one_cnt))
