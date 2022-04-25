
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R")
else:
    left = [a[0]]
    right = [a[n-1]]
    left_index = 1
    right_index = n-2
    while left_index < right_index:
        if a[left_index] > left[-1]:
            left.append(a[left_index])
            left_index += 1
        if a[right_index] > right[-1]:
            right.append(a[right_index])
            right_index -= 1
        if a[left_index] <= left[-1] and a[right_index] <= right[-1]:
            break
    if len(left) > len(right):
        print(len(left))
        print("L"*len(left))
    else:
        print(len(right))
        print("R"*len(right))
