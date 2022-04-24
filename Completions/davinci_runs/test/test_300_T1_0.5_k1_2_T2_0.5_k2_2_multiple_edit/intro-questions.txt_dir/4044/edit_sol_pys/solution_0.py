

a, b, x = map(int, input().split()) #input

s = [] #initialize list
for i in range(a):
    s.append('0')
for i in range(b):
    s.append('1')

for i in range(x): #swap 
    if i % 2 == 0:
        s[i], s[i+1] = s[i+1], s[i]
    else:
        s[-i-1], s[-i-2] = s[-i-2], s[-i-1]

print(''.join(s))
