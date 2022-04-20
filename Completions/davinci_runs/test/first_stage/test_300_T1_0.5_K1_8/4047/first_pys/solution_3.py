

# SOLUTION
n = int(input())
x = list(map(int, input().split()))

x.sort()

if x[-1] - x[0] == 0:
    print(0)
elif x[-1] - x[0] == 1:
    print(1)
elif x[-1] - x[0] == 2:
    print(1)
else:
    print(2)