

n, k = map(int, input().split()) # get input

digits = 0 # initialize

while n > 0: # iterate until N is 0
    digits += 1 # increment digit count
    n //= k # divide by k

# print result
print(digits)
