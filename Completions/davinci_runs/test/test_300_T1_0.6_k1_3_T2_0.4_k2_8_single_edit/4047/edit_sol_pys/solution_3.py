
n = int(input())
x = [int(i) for i in input().split()]  # list comprehension

if n == 1:
    print(0)
else:
    x.sort()  # sort list in ascending order
    if x[0] == x[-1]:
        print(0)
    else:
        if x[1] == x[-1]:
            print(x[-1] - x[1])  # print difference between last and second element
        else:
            print(min(x[-1] - x[1], x[-2] - x[0]))  # print min of difference between last and second element and second last and first element
