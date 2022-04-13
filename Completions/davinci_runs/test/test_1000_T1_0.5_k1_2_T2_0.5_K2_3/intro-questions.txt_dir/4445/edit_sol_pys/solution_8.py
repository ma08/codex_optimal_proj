
n = int(input())
a = list(map(int, input().split()))

# find the number of odd numbers and the number of even numbers
odd = sum([i % 2 == 1 for i in a])
even = sum([i % 2 == 0 for i in a])

# if odd is odd, find the first even number and delete it
if odd % 2 == 1 and even > 0:
    for i in range(len(a)):
        if a[i] % 2 == 0:
            print(sum(a) - a[i])
            exit()

# if odd is even, find the first odd number and delete it
if odd % 2 == 0 and odd > 0:
    for i in range(len(a)):
        if a[i] % 2 == 1:
            print(sum(a) - a[i])
            exit()
