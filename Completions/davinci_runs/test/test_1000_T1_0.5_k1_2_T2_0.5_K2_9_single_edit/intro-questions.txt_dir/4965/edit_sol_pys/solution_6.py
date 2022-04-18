
import sys

def rearrange(n, t): # t is a list of integers
    t = sorted(t) # sort the list
    if n%2 == 0: # if the list has an even number of elements
        t1 = t[:n//2] # take the first half of the list
        t2 = t[n//2:] # take the second half of the list
    else: # if the list has an odd number of elements
        t1 = t[:n//2] # take the first half of the list
        t2 = t[n//2+1:] # take the second half of the list
    t1.reverse() # reverse the first half of the list
    t1 = t1 + t2 # join the two halves of the list
    return t1 # return the new list

n = int(input())
t = [int(x) for x in input().split()]

print(*rearrange(n, t))
