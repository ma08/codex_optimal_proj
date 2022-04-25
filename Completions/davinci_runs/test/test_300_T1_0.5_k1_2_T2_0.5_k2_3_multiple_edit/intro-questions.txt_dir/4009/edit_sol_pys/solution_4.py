
n, x, y = map(int, input().split()) 
n = list(input()) # input string convert to list

if n[y] == '0': # if the yth number is 0
    n[y] = '1'
else: # if the yth number is 1
    n[y] = '0'
    for i in range(y+1, x): # from y+1 to x-1
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
