

n, x, y = map(int, input().split()) # n, x, y (n is the number of bits in the binary number, x is the position of the first bit from the right that is to be flipped, y is the position of the last bit from the right that is to be flipped)
n = list(input()) # binary number

if n[y] == '0': # if the last bit is 0, then change it to 1
    n[y] = '1'
else:
    n[y] = '0'
    for i in range(y+1, x):
        if n[i] == '0':
            n[i] = '1'
            break
        else:
            n[i] = '0'

print(n.count('0'))
