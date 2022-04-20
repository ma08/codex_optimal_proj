
n = int(input())
a = list(map(int, input().split()))
f = list(map(int, input().split()))

# build a dict of f(x)
f_dict = {}
for i in range(1, 10):
    f_dict[i] = f[i-1]

# replace each digit with f(x)
for i in range(len(a)):
    a[i] = f_dict[a[i]]

# convert a to a string and print
print(''.join(map(str, a)))
