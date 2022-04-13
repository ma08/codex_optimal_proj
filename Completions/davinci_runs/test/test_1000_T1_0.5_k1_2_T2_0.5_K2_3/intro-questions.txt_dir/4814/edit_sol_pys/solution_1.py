n = int(input())
names = input().split()
for i in range(n):
    names.append(names[i])

if names == sorted(names):
    print("INCREASING")
elif names == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
