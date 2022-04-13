

# Solution 2
for i in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == r2:
        print(l1, l2)
    else:
        print(l1, r2)
