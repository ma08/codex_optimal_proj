
n = int(input())
names = []
for i in range(n):
    names.append(input())

increasing = False
decreasing = False
if n == 1:
    increasing = True
    decreasing = True
else:
    for i in range(1, n):
        if names[i - 1] < names[i]:
            decreasing = False
        elif names[i - 1] > names[i]:
            increasing = False

if increasing:
    print("INCREASING")
elif decreasing:
    print("DECREASING")
else:
    print("NEITHER")
