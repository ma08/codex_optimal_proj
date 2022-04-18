
n = int(input())  # input n

a = list(map(int, input().split()))  # input and convert to list

a.sort()  # sort the list

for i in range(n):  # print all elements
    print(a[i], end=' ')
