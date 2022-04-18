

a, b, x = map(int, input().split()) # input a, b, x

s = [] # define list s
for i in range(a):
    s.append('0') # add '0' to list s
for i in range(b):
    s.append('1') # add '1' to list s

for i in range(x): # swap first and last
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s)) # output
