

def main():
    # Get input from user
    # n = int(input())
    # a = [int(x) for x in input().split()]

    # Solve
    # print(solve(n, a))
    print(solve(3, [2, 1, 2]))

def solve(n, a):
    # Sort a
    a.sort()
    print(a)

    # Find the number of groups
    groups = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            groups += 1

    # Find the number of elements in each group
    elements = [0] * groups
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
