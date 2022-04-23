
# this is a test
n = int(input()) # the number of elements
l = list(map(int, input().split())) # the elements

m = 0 # the max length of the sequence
d = {} # the dictionary

for i in l: # iterate through the elements
    if i in d: # if the element is already in the dictionary
        continue
    d[i] = 1 # add the element to the dictionary
    for j in range(32): # iterate through the powers of 2
        if i + 2**j in d: # if the element + 2^j is in the dictionary
            d[i + 2**j] = d[i] + 1 # add it to the dictionary with the length of the sequence
        if i - 2**j in d: # if the element - 2^j is in the dictionary
            d[i - 2**j] = d[i] + 1 # add it to the dictionary with the length of the sequence
        m = max(m, d[i]) # update the max length

print(m) # print the max length

for i in l: # iterate through the elements
    if d[i] == m: # if the length of the sequence is the max
        print(i, end=' ') # print the element
