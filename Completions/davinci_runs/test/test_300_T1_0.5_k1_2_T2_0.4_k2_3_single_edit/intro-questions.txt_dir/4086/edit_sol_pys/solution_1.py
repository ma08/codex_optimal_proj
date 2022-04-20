
n = int(input())
a = [int(x) for x in input().split()]


def remove_duplicates(a, n):
    if n == 0 or n == 1:
        return n
    temp = []
    j = 0
    for i in range(0, n - 1):
        if a[i] != a[i + 1]:
            temp.append(a[i])
            j += 1
    temp.append(a[n - 1])
    for i in range(0, j + 1):
        a[i] = temp[i]
    return j + 1

n = remove_duplicates(a, n)
print(n)
print(*a[:n])
