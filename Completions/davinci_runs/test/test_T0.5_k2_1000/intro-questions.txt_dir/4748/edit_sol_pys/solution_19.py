
h, n, m = map(int, input().split()) # h: height of the wall, n: number of bricks, m: number of bricks with a hole

a = 0 # number of bricks without a hole
b = 0 # number of bricks with a hole

for i in range(1, h+1):
    a += (2*i - 1) # number of bricks without a hole for each row
    b += (2*i) # number of bricks with a hole for each row

if a <= n:
    print(0, m) # all bricks with a hole
else:
    a -= n # number of bricks without a hole
    if a <= m*2:
        print(a//2, m - (a//2)) # number of bricks without a hole and with a hole
    else:
        print(m, 0) # all bricks without a hole
