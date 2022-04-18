"""
Given an array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.
"""

N = int(input())
A = [int(i) for i in input().split()]

for i in range(N):
    print(A.index(i+1)+1, end=' ') #end=' ' adds a space, default is new line
