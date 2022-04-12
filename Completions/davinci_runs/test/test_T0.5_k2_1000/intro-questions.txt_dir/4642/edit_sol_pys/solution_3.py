
t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    if 2*x == y:  # if difference between two numbers is equal to the sum of those two numbers
        print(x, y, end=" ")
        for j in range(3,n+1):
            print(x+y, end=" ")  # then all the numbers will be equal to the sum of first two numbers
    else:
        print(x, y, end=" ")
        l = [x, y]  # else we will find the difference between the numbers and add it to the last number to get the next number
        d = (y-x)//(n-2)  # difference between two numbers
        for j in range(n-2):
            l.append(l[-1]+d)
        for j in l:
            print(j, end=" ")
    print()
