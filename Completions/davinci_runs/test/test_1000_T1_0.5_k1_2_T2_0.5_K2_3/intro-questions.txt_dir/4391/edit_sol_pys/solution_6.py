
n,k = map(int, input().split())
a = list(map(int, input().split()))

max_sum_window = sum(a[:k])
curr_sum_window = max_sum_window
for i in range(k,n):
    curr_sum_window += a[i] - a[i-k]
    max_sum_window = max(max_sum_window, curr_sum_window)

print(max_sum_window/k)
