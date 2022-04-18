
K = int(input()) # input
S = input() # input

if len(S) > K: # if lenght of string is greater than K
    # print string from 0 to K and add '...'
    print(S[:K] + '...')
    # if lenght of string is less than K, print string
else:
    print(S)
