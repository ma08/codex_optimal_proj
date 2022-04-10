# cook your dish here

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    l = set()
    for j in range(n):
        a = input().split()
        b = input().split()
        l.add(tuple(a+b))
    if len(l) == n:
        print("NO")
    else:
        print("NO")
