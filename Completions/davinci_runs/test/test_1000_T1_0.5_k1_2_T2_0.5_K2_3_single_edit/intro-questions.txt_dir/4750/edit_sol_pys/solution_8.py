
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/
# SOLUTION

q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == r1:
        print(l1, l2)
    else:
        print(l1, r2)
