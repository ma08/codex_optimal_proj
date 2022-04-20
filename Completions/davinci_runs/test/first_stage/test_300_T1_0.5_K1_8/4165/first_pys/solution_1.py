

n = int(input())
ls = list(map(int,input().split()))

if sorted(ls)[-1] < sum(ls) - sorted(ls)[-1]:
    print('Yes')
else:
    print('No')