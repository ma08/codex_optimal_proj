

#-----main-----

S = input()

# black, white count initalize
b_cnt = 0
w_cnt = 0

# count black and white
for i in S:
    if i == '0':
        b_cnt += 1
    else:
        w_cnt += 1

# output

#-----main-----
print(min(b_cnt, w_cnt))
