

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = list(map(int, input().split()))

count = 0

i = 0
j = 0
k = 0

while k < n:
    if a[i] == b[j] + c[k]:
        count += 1
        i += 1
        j += 1
        k += 1
    elif a[i] > b[j] + c[k]:
        k += 1
    else:
        i += 1

print(count)
