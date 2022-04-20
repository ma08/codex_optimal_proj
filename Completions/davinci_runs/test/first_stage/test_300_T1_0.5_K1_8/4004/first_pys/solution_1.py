

n = int(input())
arr = list(map(int, input().split()))

min_val = min(arr)
max_val = max(arr)

if max_val - min_val > 1:
    print(-1)
else:
    print(max(0, max_val - min_val))