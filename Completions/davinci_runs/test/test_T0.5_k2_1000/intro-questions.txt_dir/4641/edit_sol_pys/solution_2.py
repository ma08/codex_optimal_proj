
import sys

def main():
    # Read in the input and parse it
    q, x = map(int, input().split())
    queries = [int(input()) for i in range(q)]

    # Initialize the array and the MEX
    arr = [0]
    mex = 0

    # Iterate through the queries
    for i in range(0, len(queries)):
        # If the new element is smaller than the MEX, we can increase it to the MEX + 1
        if queries[i] < mex:
            queries[i] += x
        # If the new element is equal to the MEX, we need to increase the MEX
        elif queries[i] == mex:
            mex += 1
        # If the new element is greater than the MEX, we can do nothing
        elif queries[i] > mex:
            pass
        # Append the new element to the array and sort it
        arr.append(queries[i])
        arr.sort()
        # Print the MEX
        print(mex)

if __name__ == '__main__':
    main()
