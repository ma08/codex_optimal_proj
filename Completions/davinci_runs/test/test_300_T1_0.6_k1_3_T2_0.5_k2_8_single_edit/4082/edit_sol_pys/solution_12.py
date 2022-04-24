
def max_increasing_subarray(a):
    max_length = 0
    length = 1
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
    return max_length+1
n = int(input())
a = list(map(int,input().split()))
max_length = max_increasing_subarray(a)
for i in range(len(a)):
    if i == 0:
        if a[i] < a[i+1]:
            a[i] = a[i+1] - 1
    elif i == len(a) - 1:
        if a[i] > a[i-1]:
            a[i] = a[i-1] + 1
    else:
        if a[i] > a[i-1] and a[i] < a[i+1]:
            a[i] = a[i-1] + 1
        elif a[i] < a[i-1] and a[i] > a[i+1]:
            a[i] = a[i+1] - 1
if max_increasing_subarray(a) > max_length:
    max_length = max_increasing_subarray(a)
print(max_length)
