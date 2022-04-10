

def find_subarray(arr, sum):
    for i in range(len(arr)):

        for j in range(i, len(arr)):
            if sum(arr[i:j+1]) == sum:
                return arr[i:j+1]
