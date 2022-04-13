
N = int(input())  # input number of elements
A = [int(i) for i in input().split()]  # input numbers and convert them to integer

for i in range(N):
    print(A.index(i+1)+1, end=' ')  # print the index of the number
