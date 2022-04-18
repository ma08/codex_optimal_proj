

n = int(input()) # num of elements in array
a = list(map(int, input().split())) # array of elements

odds = 0 # sum of odd elements
evens = 0 # sum of even elements
count = 0 # number of indices with equal sums of even and odd elements

for i in range(n): # for each element in the array
    if i % 2 == 0:
        evens += a[i] # add the element to the sum of even elements
    else:
        odds += a[i] # add the element to the sum of odd elements

for i in range(n): # for each element in the array
    if i % 2 == 0:
        evens -= a[i] # subtract the element from the sum of even elements
    else:
        odds -= a[i] # subtract the element from the sum of odd elements
    if odds == evens: # if the sums of even and odd elements are equal
        count += 1 # increase the count by 1
    if i % 2 == 0:
        evens += a[i] # add the element to the sum of even elements
    else:
        odds += a[i] # add the element to the sum of odd elements

print(count) # print the count
