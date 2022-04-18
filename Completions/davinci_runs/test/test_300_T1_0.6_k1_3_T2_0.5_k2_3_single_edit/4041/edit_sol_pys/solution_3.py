

# get the input
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# set up the answer
answer = 0

# set up the pointers
i = 0
j = 0

# loop through the sorted lists
while i < n and j < m:
    # if the current element of the first list is less than the current element of the second list,
    # move the pointer in the first list up
    if a[i] < b[j]:
        i += 1
    # if the current element of the second list is less than the current element of the first list,
    # move the pointer in the second list up
    elif b[j] < a[i]:
        j += 1
    # if the current element of the first list is equal to the current element of the second list,
    # move both pointers up and add one to the answer
    else:
        i += 1
        j += 1
        answer += 1

# output the answer, which is the number of elements in the intersection
print(answer)
