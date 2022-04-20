

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0)
    exit()

a.sort()

# if all elements are equal, we can make them all equal to any element
if a[0] == a[-1]:
    print(0)
    exit()

# if we have an odd number of elements, we cannot make them all equal
if n % 2 != 0:
    print(-1)
    exit()

# if we have an even number of elements, we can make them all equal to the middle elements
if n % 2 == 0:
    if a[n//2-1] == a[n//2]:
        print(0)
        exit()
    else:
        print(a[n//2]-a[n//2-1])
        exit()