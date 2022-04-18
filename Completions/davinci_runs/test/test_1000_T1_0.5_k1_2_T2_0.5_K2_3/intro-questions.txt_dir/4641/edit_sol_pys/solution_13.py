
import sys

def main():
    # Read in the input and convert it to an integer
    q, x = map(int, sys.stdin.readline().strip().split(' ')) # q = number of queries, x = number to add to elements
    queries = [] # list of queries
    for i in range(0, q): # loop to read queries
        queries.append(int(sys.stdin.readline().strip())) # add query to list of queries

    # Initialize the array
    arr = [] # list to store numbers

    # Iterate through the queries
    for i in range(0, len(queries)): # loop to iterate through queries
        # Append the new element to the array
        arr.append(queries[i]) # add query to list
        
        # Calculate the MEX and print it
        print(calculate_mex(arr, x), end=' ') # print MEX

def calculate_mex(arr, x): # calculate the MEX
    # Sort the array
    arr.sort() # sort the list

    # Initialize the MEX as 0
    mex = 0
    
    # Iterate through the array
    for i in range(0, len(arr)): # loop to iterate through the list
        # If the current element is smaller than the MEX, we can increase it to the MEX
        if arr[i] < mex: # if current element is less than MEX
            arr[i] += x # add x to current element
        # If the current element is equal to the MEX, we need to increase the MEX
        elif arr[i] == mex: # if current element is equal to MEX
            mex += 1 # increase MEX
        # If the current element is greater than the MEX, we can do nothing
        else: # if current element is greater than MEX
            pass
    
    # Return the MEX
    return mex

if __name__ == '__main__':
    main()
