
def main():
    # Get input
    n = int(input())  # Number of elements in the array
    a = [int(x) for x in input().split()]  # Elements in the array

    # Solve
    print(solve(n, a))

def solve(n, a):
    # Sort a in ascending order
    a = sorted(a)

    # Find the number of different elements in a
    groups = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            groups += 1

    # Find the number of elements in each group of equal elements
    elements = [0 for x in range(groups)]  # Initialize elements
    for i in range(n):
        elements[a[i]-1] += 1

        # Find the number of elements in each group
        elements[a[i]-1] += 1

    # Find the number of elements in the largest group of equal elements
    max_elements = max(elements)

    max_elements = max(elements)

    # Find the number of groups of equal elements that contain the largest
    # number of elements
    max_groups = 0
    for i in range(groups):
        if elements[i] == max_elements:  # Check if current group has the
            max_groups += 1              # largest number of elements

    # Return the answer
    return max_elements * max_groups

if __name__ == '__main__':
    main()
