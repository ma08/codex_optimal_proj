

n = int(input())
x = list(map(int, input().split()))
mx = max(x)
mn = min(x)

if mx == mn:
    print(0)
else:
    print(mx-mn-n)