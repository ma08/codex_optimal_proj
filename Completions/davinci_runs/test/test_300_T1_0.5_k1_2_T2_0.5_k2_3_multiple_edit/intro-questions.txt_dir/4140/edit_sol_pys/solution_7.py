
#-----main-----

S = input()

# black count
b_cnt = S.count('0')

# white count
w_cnt = S.count('1')

# output
print(min(b_cnt, w_cnt))
