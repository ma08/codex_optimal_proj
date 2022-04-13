
# read input
c, k = map(int, input().split())
# check if the last k digits are greater than or equal to 5*10**(k-1)

if c % 10**k >= 5*10**(k-1):
    print(c + (10**k - c % 10**k))
else:



    print(c - c % 10**k)
