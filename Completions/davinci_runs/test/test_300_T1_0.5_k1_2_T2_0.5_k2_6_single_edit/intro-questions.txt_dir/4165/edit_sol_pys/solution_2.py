

n = int(input())

l = list(map(int, input().split()))
s = sum(l)
if max(l) < s-max(l):
    print("Yes")
else:
    print("No")
