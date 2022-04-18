
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left, right = 0, n-1
    for i in range(n):
        if a[i] == 1 and left == 0:
            left = i
            break
    for i in range(n-1, -1, -1):
        if a[i] == 1 and right == n-1:
            right = i
            break
    # print(left, right)
    if left == right:
        print(0)
    else:
        # print(a[left:right+1])
        # print(sum(a[left:right+1]))
        print(right-left - sum(a[left:right+1]))
