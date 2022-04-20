

N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)
# print(L)

if L[0] < sum(L[1:]):
    print('Yes')
else:
    print('No')