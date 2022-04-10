n, m = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = sorted(arr)

if n % 2 == 0:
    median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
else:
    median = sorted_arr[n // 2]

if median != m:
    print(0)
    exit()

count = 0

left_pointer = 0
right_pointer = n - 1

while left_pointer <= right_pointer:
    if arr[left_pointer] == m:
        count += 1
        left_pointer += 1
    elif arr[right_pointer] == m:
        count += 1
        right_pointer -= 1
    else:
        left_pointer += 1
        right_pointer -= 1

print(count)
