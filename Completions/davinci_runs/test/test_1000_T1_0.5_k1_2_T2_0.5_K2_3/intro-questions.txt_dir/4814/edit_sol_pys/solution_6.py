n = int(input())
names = []
for i in range(n):
    names.append(input().strip())

if names == sorted(names, key=str.lower):
    print("INCREASING")
elif names == sorted(names, key=str.lower, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
