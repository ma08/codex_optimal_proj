

def main():
    # Get input
    n = int(input())
    a = [int(x) for x in input().split()] # List of integers

    # Solve
    print(solve(n, a)) # Print the answer

def solve(n, a):
    # Sort the list
    a = sorted(a) # a is now sorted

    # Find the number of groups in the list
    groups = 1 # There is at least one group
    for i in range(n-1):
        if a[i] != a[i+1]: # If the current element is not equal to the next element, then there is another group
            groups += 1

    # Find the number of elements in each group in the list
    elements = [0 for x in range(groups)] # Initialize the list of elements
    for i in range(n):
        elements[a[i]-1] += 1 # Increment the number of elements in the group

    max_elements = max(elements) # The maximum number of elements in any group

    # Find the number of groups that contain the maximum number of elements
    max_groups = 0 # Initialize the number of groups that contain the maximum number of elements
    for i in range(groups):
        if elements[i] == max_elements: # If the number of elements in the current group is equal to the maximum number of elements, then increment the number of groups that contain the maximum number of elements
            max_groups += 1

    # Return the answer (the maximum number of elements in any group times the number of groups that contain the maximum number of elements)
    return max_elements * max_groups # Return the answer

if __name__ == '__main__':
    main() # Run the program
