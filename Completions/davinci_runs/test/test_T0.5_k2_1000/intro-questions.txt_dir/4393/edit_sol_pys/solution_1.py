
n = int(input()) # number of elements
t = input() # input string
s = [] # output string

for i in range(n): # loop through the input string
    if t[i] != t[i-1]:
        s.append(t[i]) # append to output string

print(''.join(s)) # print output string
