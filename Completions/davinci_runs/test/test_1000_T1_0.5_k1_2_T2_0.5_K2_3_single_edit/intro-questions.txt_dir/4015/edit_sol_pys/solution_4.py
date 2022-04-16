
#-----Solution-----

#This is a greedy algorithm.
#The idea is to greedily multiply by 3 until the number is greater than m.
#Then, multiply by 2 as many times as possible, until the number is greater than m.
#If the number is not m, then the answer is -1.

n, m = map(int, input().split())  #take input

if n == m:
    print(0)  #if n = m, then print 0
elif m % 2 == 0 and n % 2 == 1:
    print(-1)  #if n is odd and m is even, then print -1
else:
    steps = 0  #initialize steps to 0
    while n < m:
        if n * 3 <= m:  #if n * 3 is less than or equal to m
            n *= 3  #multiply n by 3
        else:
            n *= 2  #else, multiply n by 2
        steps += 1  #increment steps
    if n == m:  #if n = m
        print(steps)  #print steps
    else:
        print(-1)
