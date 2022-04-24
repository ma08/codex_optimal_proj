

# get input as array
l = input().split(' ')

# get length of array
l_len = len(l)

# loop through array
for i in range(0, l_len):
    # get the number
    num = int(l[i])
    # check if it's divisible by 2
    if num % 2 == 0:
        # print the number
        print(num)

# print out result
print(l)
