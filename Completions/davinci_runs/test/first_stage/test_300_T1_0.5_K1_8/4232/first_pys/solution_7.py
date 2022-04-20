

#-----Solution-----

#This solution is based on binary search

n, k = map(int, input().split())
arr = list(map(int, input().split()))

#Sorts the array
arr.sort()

#Sets the left and right bounds
left = 1
right = 10**9

#Sets the value to -1
value = -1

#While the left bound is less than the right bound
while left <= right:
    #Sets the middle value
    mid = (left + right) // 2

    #Sets the count to 0
    count = 0

    #For each element in the array
    for i in arr:
        #If the element is less than or equal to the middle value
        if i <= mid:
            #Increment the count
            count += 1

    #If the count is equal to the k value
    if count == k:
        #Set the value to the middle value
        value = mid
        #Break the loop
        break
    #If the count is less than the k value
    elif count < k:
        #Set the left bound to the middle value + 1
        left = mid + 1
    #If the count is greater than the k value
    else:
        #Set the right bound to the middle value - 1
        right = mid - 1

#Print the value
print(value)