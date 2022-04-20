

def solve(a, n):
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        if mid == 1:
            return 1
        if mid == n:
            return n
        if a[mid] == a[mid - 1] and a[mid] == a[mid + 1]:
            return mid
        if a[mid] < a[mid - 1]:
            r = mid - 1
        elif a[mid] > a[mid - 1]:
            l = mid + 1
        else:
            l = mid + 1
            r = mid - 1


n = int(input())
a = list(map(int, input().split()))
print(solve(a, n))