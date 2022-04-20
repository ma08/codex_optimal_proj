
n = int(input())
h = list(map(int, input().split()))
if n == 1:
    print('Yes')
else:
    print('Yes' if all(h[i] <= h[i+1] for i in range(n-1)) or all(h[i] == h[i+1]+1 for i in range(n-1)) else 'No')
