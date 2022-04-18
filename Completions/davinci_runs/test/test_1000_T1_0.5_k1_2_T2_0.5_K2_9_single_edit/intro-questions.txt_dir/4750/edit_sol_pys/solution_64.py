
# Solution
"""
1. If ranges are not overlapping, then a = l1, b = l2
2. If ranges are overlapping, then a = l1, b = r2
3. If ranges are identical, then a = l1, b = r2
"""
q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 < l2:
        a = l1
        b = l2
    else:
        a = l2
        b = l1

    print(a, b)
