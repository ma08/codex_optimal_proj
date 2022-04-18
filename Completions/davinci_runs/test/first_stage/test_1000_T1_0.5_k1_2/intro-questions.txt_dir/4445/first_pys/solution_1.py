

n = int(input())
a = list(map(int, input().split()))

# find the odd number of odd numbers
odd = 0
for i in a:
    if i % 2 == 1:
        odd += 1

# if odd is odd, find the first even number and delete all the others
if odd % 2 == 1:
    for i in range(len(a)):
        if a[i] % 2 == 0:
            print(sum(a) - a[i])
            exit()

# if odd is even, find the first odd number and delete all the others
if odd % 2 == 0:
    for i in range(len(a)):
        if a[i] % 2 == 1:
            print(sum(a) - a[i])
            exit()