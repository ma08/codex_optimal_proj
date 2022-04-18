
# test
# SOLUTION

queries = int(input())
for _ in range(queries):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == r1:
        print(l1, l2)
    else:
        print(l1, r2)
