
n = int(input())  # number of elements
l = list(map(int, input().split()))  # list of elements
if max(l) < sum(l)-max(l):  # if the max element is less than the sum of all elements minus the max element
    print("Yes")  # print yes
else:  # otherwise
    print("No")  # print no
