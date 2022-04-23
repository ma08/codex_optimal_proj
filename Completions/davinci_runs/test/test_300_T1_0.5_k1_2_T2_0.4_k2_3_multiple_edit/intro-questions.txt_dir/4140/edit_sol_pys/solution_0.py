

S = input()

# black, white counts
b_cnt = 0
w_cnt = 0

# count black and whites
for i in S:
    if i == '0':
        b_cnt += 1
    else:
        w_cnt += 1

# output
print(min(b_cnt, w_cnt))
