

n = int(input())  # number of elements in the array
array = list(map(int, input().split()))  # array of n elements

def min_instability(n, array):
    array.sort()  # sort the array
    min_instability = array[-1] - array[0]  # initialize min instability to the difference between the first and last elements

    for i in range(1, n-1):
        if array[i] - array[i-1] < min_instability:  # if the difference between the current element and the previous element is less than the current min instability
            min_instability = array[i] - array[i-1]  # set the min instability to that difference
        if array[i+1] - array[i] < min_instability:  # if the difference between the next element and the current element is less than the current min instability
            min_instability = array[i+1] - array[i]  # set the min instability to that difference
    return min_instability  # return the min instability

print(min_instability(n, array))
