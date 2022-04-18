

#----CODE----

#input
N = int(input())
A_list = list(map(int, input().split()))

#finds the max diff between two elements in a list
def find_max_diff(A):
    max_diff = A[1] - A[0]
    min_element = A[0]

    for i in range(1, N):
        if A[i] - min_element > max_diff:
            max_diff = A[i] - min_element
        if A[i] < min_element:
            min_element = A[i]
    return max_diff 

print(find_max_diff(A_list))
