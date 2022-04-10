

n = int(input())
x = [int(i) for i in input().split()]
x.sort()

if n == 1:
    print(0)
elif n == 2:
    print(abs(x[0] - x[1]) // 2)
else:
    if x[0] == x[n - 1]:
        print(0)
    elif x[0] == x[1]:
        print(abs(x[0] - x[n - 1]) // 2)
    elif x[n - 2] == x[n - 1]:
        print(abs(x[0] - x[n - 1]) // 2)
    else:
        print(min(abs(x[0] - x[n - 2]), abs(x[1] - x[n - 1])) // 2 + 1)