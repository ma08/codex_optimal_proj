

# -----main-----

S = input()

# black, white
b = 0
w = 0

# count black and white
for i in S:
    if i == '0':
        b += 1
    else:
        w += 1

# output
print(min(b, w))
