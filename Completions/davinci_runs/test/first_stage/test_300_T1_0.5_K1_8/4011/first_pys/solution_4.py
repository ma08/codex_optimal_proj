

N = int(input())
a = input()
f = list(map(int, input().split()))

# find the first digit that can be increased
i = 0
while a[i] == '9' or f[int(a[i])-1] <= int(a[i]):
    i += 1

# find the last digit that can be increased
j = N - 1
while a[j] == '9' or f[int(a[j])-1] <= int(a[j]):
    j -= 1

# replace the digits in the range [i, j]
for k in range(i, j+1):
    a = a[:k] + str(f[int(a[k])-1]) + a[k+1:]

print(a)