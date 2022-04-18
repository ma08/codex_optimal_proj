# a little program to check if a list of numbers can be divided into two groups such that the sum of both groups is equal.

n = int(input())

l = list(map(int, input().split()))

if max(l) < sum(l)-max(l):
    print("Yes")
else:
    print("No")
