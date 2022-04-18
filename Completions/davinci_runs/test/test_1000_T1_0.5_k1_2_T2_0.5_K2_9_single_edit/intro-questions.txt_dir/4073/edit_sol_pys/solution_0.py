

def main():
    # Get input from file
    with open('input.txt') as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]

    # Solve
    answer = solve(n, a)

    # Print answer
    print(answer)

    # Save answer to file
    with open('output.txt', 'w') as f:
        f.write(str(answer))

def solve(n, a):
    # Sort a
    a = sorted(a)

    # Find the number of groups
    groups = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            groups += 1

    # Find the number of elements in each group
    elements = [0 for x in range(groups)]
    for i in range(n):
        elements[a[i]-1] += 1

    # Find the number of elements in the largest group
    max_elements = max(elements)

    # Find the number of groups that contain the largest number of elements
    max_groups = 0
    for i in range(groups):
        if elements[i] == max_elements:
            max_groups += 1

    # Return the answer
    return max_elements * max_groups

if __name__ == '__main__':
    main()
