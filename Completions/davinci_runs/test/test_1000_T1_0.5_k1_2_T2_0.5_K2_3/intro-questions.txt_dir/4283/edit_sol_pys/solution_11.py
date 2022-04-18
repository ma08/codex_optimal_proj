n = int(input())  # number of elements in array
a = list(map(int, input().split()))  # array of elements
a.sort()  # sorting the array

if n == 1:  # if the array has only one element
    print(1)
    exit(0)

i = 0  # pointer to first element
j = 1  # pointer to second element

count = 0
while j < n:
    if a[j] - a[i] <= 5:
        j += 1
    else:
        i = j
        j += 1
    count = max(count, j - i)

print(count)
