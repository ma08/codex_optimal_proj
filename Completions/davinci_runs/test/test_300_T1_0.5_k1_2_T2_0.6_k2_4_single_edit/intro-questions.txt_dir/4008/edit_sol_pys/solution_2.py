
n, k = map(int, input().split())  # n: number of elements in the list, k: number of distinct values
a = list(map(int, input().split()))  # list of numbers
if n == 1:  # if there is only one element, we can always split
    print("YES")  # print yes
    print(1)  # print 1
else:  # if there is more than one element, we have to check
    b = [0]*n  # create an empty list with the same length as the input list
    for i in range(n):  # loop through the list
        if a[i] == a[0]:  # if the current element is equal to the first element
            b[i] = 1  # put 1 in the list
        else:  # if the current element is not equal to the first element
            b[i] = 2  # put 2 in the list
    if a[0] in a[1:]:  # if the first element is present in the rest of the list
        print("NO")  # we can't split the list
    else:  # if the first element is not present in the rest of the list
        print("YES")  # we can split the list
        print(*b)  # print the list
