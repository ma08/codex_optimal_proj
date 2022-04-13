# print the odd number
n = int(input()) # get the input
ans = 0          # init the answer
for i in range(1, n+1): # loop from 1 to n
    if i % 2 == 0:  # check the number is odd or not
        ans = i     # assign the value to answer
print(ans)         # print the answer
