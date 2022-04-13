

x = int(input())
n = int(input())
p = list(map(int, input().split()))

p.sort()

if x < p[0]:
    print(p[0] - x)
elif x > p[n-1]:
    print(x - p[n-1])
else:
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:
            if abs(p[i-1] - x) < abs(p[i] - x):
                print(p[i-1] - x)
            else:
                print(p[i] - x)
            break


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left, right)


a = [5, 2, 4, 6, 1, 3]
print(mergesort(a))
