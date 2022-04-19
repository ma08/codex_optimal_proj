
from fractions import gcd

def main():
    n = int(input()) # number of elements
    a = [int(i) for i in input().split()] # list of elements
    g = a[0] # gcd
    for i in range(1, n): # loop through the list
        g = gcd(g, a[i]) # calculate gcd
    print(g) # print gcd

main()
