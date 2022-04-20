

n = int(input())
a = list(map(int, input().split()))

# a = [1,3,3,7]
# a = [1,100000]

# print(a)

a.sort()
# print(a)

if len(a) == 2:
    print(0)
else:
    print(min(a[-1] - a[1], a[-2] - a[0]))