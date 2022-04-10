

n = int(input())
a = input()
f = list(map(int, input().split()))

# if the function is the identity, then we can't do anything
if f == list(range(1, 10)):
    print(a)
    exit()

# if the function is the reverse identity, then we can make all the digits 9
if f == list(range(9, 0, -1)):
    print(9 * n)
    exit()

# if the function is the constant function with value 1, then we can make all the digits 1
if f == [1] * 9:
    print(1 * n)
    exit()

# if the function is the constant function with value 9, then we can make all the digits 9
if f == [9] * 9:
    print(9 * n)
    exit()

# otherwise, we can't do anything
print(a)