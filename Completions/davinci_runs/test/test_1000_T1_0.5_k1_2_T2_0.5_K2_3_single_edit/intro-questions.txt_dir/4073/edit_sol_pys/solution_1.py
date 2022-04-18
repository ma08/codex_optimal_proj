

def main():
    # Get input
    n = int(input())
    a = [int(x) for x in input().split()]
    # Sort a
    a = sorted(a)

    # Find the number of groups
    groups = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            groups += 1

    # Find the number of elements in each group (including the largest group)
    elements = [0 for i in range(groups)]
    for i in range(n):
        elements[a[i]-1] += 1

    max_groups = elements.count(max(elements))

    # Return the answer
    return max(elements) * max_groups

if __name__ == '__main__':
    main()
