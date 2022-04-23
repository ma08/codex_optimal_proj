
# n = int(input())
# a = input()
# f = list(map(int, input().split()))

# convert a to a list of ints
a = [int(x) for x in a]

# build a dict of f(x)
f_dict = {}
for i in range(1, 10):
    f_dict[i] = f[i-1]

# replace each digit with f(x)
# e.g. a = [3,3]  f_dict = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}
for i in range(len(a)):
    a[i] = f_dict[a[i]]

# convert a to a string and print
print(''.join(map(str, a)))
