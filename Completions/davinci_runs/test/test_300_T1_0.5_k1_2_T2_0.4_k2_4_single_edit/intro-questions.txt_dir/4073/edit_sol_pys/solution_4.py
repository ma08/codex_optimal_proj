

def main():
    # Get input and solve
    print(solve(int(input()), [int(x) for x in input().split()]))


def solve(n, a):
    # Find the number of groups
    groups = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            groups += 1

    # Find the number of elements in each group
    elements = [0 for x in range(groups)]
    for i in range(groups):
        elements[i] = a.count(i + 1)

    # Find the number of elements in the largest group
    max_elements = max(elements)

    # Return the answer
    return max_elements * elements.count(max_elements)

if __name__ == '__main__':
    main()
