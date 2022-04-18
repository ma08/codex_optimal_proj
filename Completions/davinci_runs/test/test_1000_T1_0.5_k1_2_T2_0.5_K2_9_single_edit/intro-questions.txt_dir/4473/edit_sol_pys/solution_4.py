
# cook your dish here
for i in range(int(input())):
    n = int(input())
    if n == 1:
        print(0)
    elif n < 4:
        print(1)
    else:
        print(n-2)
