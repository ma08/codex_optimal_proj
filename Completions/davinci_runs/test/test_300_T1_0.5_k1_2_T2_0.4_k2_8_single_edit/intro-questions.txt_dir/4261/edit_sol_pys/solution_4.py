

n = int(input())
a = [0] + list(map(int, input().split()))
m = int(input())
for i in range(m):
    l, r = map(int, input().split())
    print(sum(a[l:r+1]))
