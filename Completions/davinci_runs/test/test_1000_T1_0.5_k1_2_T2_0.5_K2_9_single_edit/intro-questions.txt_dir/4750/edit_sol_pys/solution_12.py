

# for i in range(int(input())):
#     l1, r1, l2, r2 = map(int, input().split())
#     print(l1, l2)


# Solution
# Solution
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print(l[-1] - l[0])
