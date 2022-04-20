

n = int(input())  # input size
x = [int(i) for i in input().split()]  # input list

if n == 1:
    print(0)
else:
    x.sort()  # sort list
    if x[0] == x[-1]:
        print(0)
    else:
        if x[1] == x[-1]:
            print(x[-1] - x[1])
        else:
            print(min(x[-1] - x[1], x[-2] - x[0]))
