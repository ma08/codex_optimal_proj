

def main():
    # Get the number of test cases
    t = int(input())

    # Solve each test case
    for i in range(t):
        # Get input
        n = int(input())
        a = [int(x) for x in input().split()]

        # Solve
        print(solve(n, a))

def solve(n, a): # a is a list of integers
    # Sort a (ascending)
    a.sort()

    # Find the number of groups (elements)
    groups = 0
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            groups += 1

    # Find the number of elements in each group
    elements = [0 for x in range(groups)] # elements[i] is the number of elements in group i+1
    group = 1
    for i in range(n):
        if i == 0 or a[i] != a[i-1]:
            group = 1
        else:
            group += 1
        elements[group-1] += 1

    # Find the number of elements in the largest group
    max_groups = 0
    max_elements = max(elements)

    # Find the number of groups that contain the largest number of elements
    max_groups = 0
    for i in range(groups):
        if elements[i] == max_elements:
            max_groups += 1

            max_groups += 1

    # Return the answer (the number of elements in the largest group times the number of groups that contain the largest number of elements)
    return max_elements * max_groups # the number of elements in the largest group times the number of groups that contain the largest number of elements

if __name__ == '__main__':
    main()
