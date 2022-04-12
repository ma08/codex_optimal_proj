

h, n, m = map(int, input().split()) # h: height of the building, n: number of the broken bricks, m: number of the bricks that can be removed in the odd layer

a = 0 # number of the bricks that can be removed in the odd layer
b = 0 # number of the bricks that can be removed in the even layer

for i in range(1, h+1): # calculate the number of the bricks that can be removed
    a += (2*i - 1) # number of the bricks that can be removed in the odd layer
    b += (2*i) # number of the bricks that can be removed in the even layer

if a <= n: # if the number of the bricks that can be removed is less than the number of the broken bricks, the building cannot be removed
    print(0, m) # print the number of the bricks that can be removed
else:
    a -= n # calculate the number of the bricks that can be removed
    if a <= m*2: # if the number of the bricks that can be removed is less than the number of the bricks that can be removed
        print(a//2, m - (a//2)) # print the number of the bricks that can be removed
    else:
        print(m, 0) # print the number of the bricks that can be removed
