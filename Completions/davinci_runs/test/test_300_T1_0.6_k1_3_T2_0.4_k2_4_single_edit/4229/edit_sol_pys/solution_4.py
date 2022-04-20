

N = int(input()) # input number

sum = 0 # initialize sum

for i in range(1, N+1): # loop from 1 to N
    if i % 3 == 0 and i % 5 == 0:
        continue # skip if i is divisible by 3 and 5
    elif i % 3 == 0:
        continue # skip if i is divisible by 3
    elif i % 5 == 0:
        continue # skip if i is divisible by 5
    else:
        sum += i # add i to sum

print(sum) # print sum
