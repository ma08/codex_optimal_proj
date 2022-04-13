
n, k = map(int, input().split()) # n = number of elements in the array, k = the k th smallest element
a = list(map(int, input().split())) # array

l = 1
r = 10**9

while l <= r:
    m = (l+r)//2
    if sum(1 for x in a if x <= m) >= k:
        r = m-1
    else:
        l = m+1

if sum(1 for x in a if x <= l) == k:
    print(l)
else:
    print(-1)
