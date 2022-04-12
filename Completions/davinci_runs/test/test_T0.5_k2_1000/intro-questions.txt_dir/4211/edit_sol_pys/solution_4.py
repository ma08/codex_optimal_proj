
n = int(input())  # input the number of elements
b = list(map(int, input().split()))  # input the elements

a = []  # empty list

for i in range(n-1):  # loop over the elements
    if b[i] <= b[i+1]:  # if element is less than the next element
        a.append(b[i])  # append the element
    else:
        a.append(b[i+1])  # else append the next element

a.append(b[n-2])

print(sum(a))
