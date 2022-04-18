
n, k, q = map(int, input().split())
a = [k]*n
for i in range(q):
    a[int(input())-1] -= 1
for i in range(n):
    if a[i] <= 0:
        print("No")
    else:
        print("Yes")
