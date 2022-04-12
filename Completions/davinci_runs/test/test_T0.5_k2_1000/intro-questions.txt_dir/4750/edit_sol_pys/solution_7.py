

# SOLUTION

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if a == b:
        print(a, c)
    else:
        print(a, d)
