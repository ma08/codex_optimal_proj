

n = int(input())

l = list(map(int, input().split()))[:n]

if max(l) < sum(l)-max(l):
    print("Yes")
else:
    print("No")
