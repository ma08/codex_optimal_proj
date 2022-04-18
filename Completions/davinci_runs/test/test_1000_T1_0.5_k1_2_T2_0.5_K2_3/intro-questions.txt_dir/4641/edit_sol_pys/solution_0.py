

import sys

def main():
    # Read in the input
    q, x = map(int, sys.stdin.readline().strip().split(' '))
    queries = []
    for i in range(0, q):
        queries.append(int(sys.stdin.readline().strip()))

    # Initialize the array
    arr = []

    # Iterate through the query
    for i in range(0, len(queries)):
        # Append the new element to the array
        arr.append(queries[i])
        
        # Calculate the MEX
        print(calculate_mex(arr, x))

def calculate_mex(arr, x):
    # Sort the array
    arr.sort()

    # Initialize the MEX as 0
    mex = 0
    
    # Iterate through the array
    for i in range(0, len(arr)):
        # If the current element is smaller than the MEX, we can increase it to the MEX
        if arr[i] < mex:
            arr[i] = mex
        # If the current element is equal to the MEX, we need to increase the MEX
        elif arr[i] == mex:
            mex += 1
        # If the current element is greater than the MEX, we can do nothing
        else:
            pass
    
    # Return the MEX
    return mex

if __name__ == '__main__':
    main()
