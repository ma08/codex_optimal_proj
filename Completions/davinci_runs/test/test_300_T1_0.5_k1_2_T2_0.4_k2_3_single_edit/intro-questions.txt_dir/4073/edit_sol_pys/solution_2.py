

def main():
    # Get input
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]    

    # Solve
    print(solve(n, m, a))

def solve(n, m, a):
    # Sort a
    a = sorted(a)

    # Find the number of elements in each group
    elements = [0 for x in range(m)]
    for i in range(n):
        elements[a[i]-1] += 1

    print(elements)

    # Find the number of elements in the largest group
    max_elements = max(elements)

    # Find the number of groups that contain the largest number of elements
    max_groups = 0
    for i in range(m):
        if elements[i] == max_elements:
            max_groups += 1

    # Return the answer
    return max_elements * max_groups

if __name__ == '__main__':
    main()
