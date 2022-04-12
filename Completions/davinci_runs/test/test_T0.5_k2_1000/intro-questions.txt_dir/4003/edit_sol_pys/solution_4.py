

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    print("R", end="")
else:
    left = [a[0]]
    right = [a[n-1]]
    left_i = 1
    right_i = n-2
    while left_i < right_i:
        if a[left_i] > left[-1]:
            left.append(a[left_i])
            left_i += 1
        if a[right_i] > right[-1]:
            right.append(a[right_i])
            right_i -= 1
        if a[left_i] <= left[-1] and a[right_i] <= right[-1]:
            break
    if len(left) > len(right):
        print(len(left))
        print("L"*len(left), end="")
    else:
        print(len(right))
        print("R"*len(right), end="")
