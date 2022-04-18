# a little program to check if a list of numbers can be divided into two groups such that the sum of both groups is equal.

n = int(input())  # number of elements in the list

l = list(map(int, input().split()))  # list of elements

if max(l) < sum(l)-max(l):
    print("Yes")
else:
    print("No")
