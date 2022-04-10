

# n,k,x = map(int,input().split())
# a = list(map(int,input().split()))

n,k,x = 4,3,1
a = [1,100,1,1]

def solve(n,k,x,a):
    if x<k:
        return -1
    if x==k:
        return sum(a[:x])
    if x>k:
        return max(sum(a[:k]),sum(a[k:x]))

print(solve(n,k,x,a))