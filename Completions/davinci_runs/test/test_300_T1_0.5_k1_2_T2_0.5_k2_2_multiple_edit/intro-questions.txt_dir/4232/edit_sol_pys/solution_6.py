

n, k = map(int, input().split()) #accepting input
a = list(map(int, input().split())) #accepting input

l = 1 #left pointer
r = 10**9 #right pointer

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
