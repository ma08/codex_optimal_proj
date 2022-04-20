
a = list(map(int, input().split()))
n = int(input())

if max(a) < sum(a)-max(a):
    print("Yes")
else:
    print("No")
