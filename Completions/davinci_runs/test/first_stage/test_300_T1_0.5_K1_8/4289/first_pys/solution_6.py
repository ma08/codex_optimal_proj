

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

min_abs = float('inf')
for i, h_i in enumerate(h):
    abs_diff = abs(t - h_i * 0.006 - a)
    if abs_diff < min_abs:
        min_abs = abs_diff
        min_i = i
print(min_i + 1)