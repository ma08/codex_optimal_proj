
# Python3 program to find minimum number of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps(arr, n):
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    # Find the minimum number of jumps to reach arr[i]
    # from arr[0], and assign this value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, size))


import math

def minJumps(arr, n):
    # jumps[0] will hold the result
    jumps = [0 for i in range(n)]

    if (n == 0) or (arr[0] == 0):
        return float('inf')

    jumps[0] = 0

    # Find the minimum number of jumps to reach arr[i]
    # from arr[0], and assign this value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n - 1]


# Driver program to test above function
arr = [1, 3, 6, 3, 2, 3, 6, 8, 9, 5]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, size))

# This code is contributed by Anant Agarwal.
