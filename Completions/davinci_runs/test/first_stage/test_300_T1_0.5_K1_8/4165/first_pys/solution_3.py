

n = int(input())
l = list(map(int, input().split()))
l.sort()

s = sum(l[:n-1])
if l[n-1] < s:
    print('Yes')
else:
    print('No')