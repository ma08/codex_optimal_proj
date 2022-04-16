

import sys

def main():
    # Read in the input and store it in an array
    input = sys.stdin.readlines()
    n = int(input[0])
    arr = map(int, input[1].strip().split(' '))

    # Calculate the MEX
    print(calculate_mex(arr))
    
def calculate_mex(arr):
    # Sort the array
    arr.sort()

    # Initialize the MEX as 0
    mex = 0
    
    # Iterate through the array
    for i in range(0, len(arr)):
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
