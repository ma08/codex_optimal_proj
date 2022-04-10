
n = int(input())
b = list(map(int, input().split()))

# if the number of elements is 1 or 2, then it is already an AP
if n < 3:
    print(0)

# if the difference between the first and second element is equal to the difference between the third and second element, then it is an AP, so we don't need to change anything
elif b[1] - b[0] == b[2] - b[1]:
    print(0)

# if the difference between the first and second element is smaller than the difference between the third and second element, then we need to increase the first element
elif b[1] - b[0] < b[2] - b[1]:
    b[0] += b[2] - b[1]
    # if the first element is greater than 10^9, then it is impossible
    if b[0] > 10**9:
        print(-1)
    else:
        print(1)

# if the difference between the first and second element is greater than the difference between the third and second element, then we need to decrease the first element
elif b[1] - b[0] > b[2] - b[1]:
    b[0] -= b[2] - b[1]
    # if the first element is less than 0, then it is impossible
    if b[0] < 0:
        print(-1)
    else:
        print(1)
