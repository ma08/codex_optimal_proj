import sys

n = int(input())
a = list(map(int, input().split()))
a.append(a[0]) # add first element to the end
a.append(a[1]) # add second element to the end

best = 0 # current best
length = 0 # current length

for i in range(n + 2): # iterate through array
    if a[i] == 1:
        length += 1 # increase length
    else:
        best = max(best, length) # update best
        length = 0 # reset length

print(best) # print best
