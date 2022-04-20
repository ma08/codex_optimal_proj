

def main():
    # Get the number of elements

    # Get the elements
    n = int(input())
    a = [int(x) for x in input().split()]

    # Solve and print the answer
    print(solve(n, a))

def solve(n, a):
    # Sort the elements
    a = sorted(a)

    # Find the number of groups of elements
    groups = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            groups += 1

    # Find the number of elements in each group of elements
    elements = [0 for x in range(groups)]
    for i in range(n):
        elements[a[i]-1] += 1

        elements[a[i]-1] += 1

    # Find the number of elements in the largest group of elements
    max_elements = max(elements)

    # Find the number of groups of elements that contain the largest number of elements
    max_groups = 0
    for i in range(groups):
        if elements[i] == max_elements:
            max_groups += 1

    # Return the answer
    return max_elements * max_groups

if __name__ == '__main__':
    main()
