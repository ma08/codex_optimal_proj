

#Solution:

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(2)
else:
    longest = 0
    for i in range(1, n - 1):
        l = 1
        r = 1
        if a[i] > a[i - 1]:
            l = 2
        if a[i] > a[i + 1]:
            r = 2
        tmp = l + r
        if a[i - 1] < a[i + 1]:
            tmp -= 1
        if tmp > longest:
            longest = tmp
    print(longest)