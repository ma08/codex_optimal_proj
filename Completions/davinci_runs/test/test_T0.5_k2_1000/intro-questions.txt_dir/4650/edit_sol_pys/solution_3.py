#!/usr/bin/python3

t = int(input()) # number of test cases

for i in range(t):
    n = int(input()) # size of array
    a = list(map(int, input().split())) # array
    a.sort()
    count = 0 # number of triplets
    for j in range(n):
        if a[j] % 3 == 0: # if a[j] is divisible by 3
            count += 1
    for j in range(n):
        for k in range(j+1, n): # for all elements after a[j]
            if (a[j]+a[k]) % 3 == 0: # if a[j]+a[k] is divisible by 3
                count += 1
                break # break out of inner loop
    print(count)
