
N = int(input()) # number of test cases
L = list(map(int, input().split())) # input of integers

L.sort() # sort the list

if L[0] + L[1] > L[-1]:
    print("Yes")
else:
    print("No")
