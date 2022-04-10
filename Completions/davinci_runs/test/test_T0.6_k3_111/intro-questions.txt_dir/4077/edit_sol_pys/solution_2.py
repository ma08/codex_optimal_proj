

# -----Solution-----

n, m = map(int, input().split())
a = list(map(int, input().split()))
result = 0

for i in range(n):
    start = i
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if a[mid] == m:
            temp_mid = mid
            while temp_mid > 0 and a[temp_mid - 1] == m:
                temp_mid -= 1
            temp_start = start
            while temp_start < mid and a[temp_start] < m:
                temp_start += 1
            result += (mid - temp_mid + 1) * (temp_mid - temp_start + 1)
            break
        elif a[mid] < m:
            start = mid + 1
        else:
            end = mid - 1

print(result)
