
n = int(input())
l = list(map(int, input().split()))

if max(l) < sum(l) - max(l) and n != 1:
    print('Yes')
else:
    print('No')
