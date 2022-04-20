

n = int(input())

# create list of lists of size 2
a = [[0,0] for i in range(n)]

# populate the list of lists
for i in range(n):
    a[i][0], a[i][1] = map(int, input().split())

# create a list of size n
p = [0 for i in range(n)]

# p[0] can be any value from 1 to n
# we will just choose 1 arbitrarily
p[0] = 1

# populate the rest of the list
for i in range(1,n):
    # if the value of the previous element in p is the same
    # as the first element in a[i], then the value of the
    # current element in p should be the second element in a[i]
    if p[i-1] == a[i][0]:
        p[i] = a[i][1]
    # otherwise, the value of the current element in p
    # should be the first element in a[i]
    else:
        p[i] = a[i][0]

# print the list p
for i in range(n):
    print(p[i], end=" ")
print()