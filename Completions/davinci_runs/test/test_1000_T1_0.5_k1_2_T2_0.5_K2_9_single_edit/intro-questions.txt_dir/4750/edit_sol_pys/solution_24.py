# SOLUTION

q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())  # take input
    if l1 == r1:  # condition
        print(l1, l2)  # print
    else:  # condition
        print(l1, r2)  # print
