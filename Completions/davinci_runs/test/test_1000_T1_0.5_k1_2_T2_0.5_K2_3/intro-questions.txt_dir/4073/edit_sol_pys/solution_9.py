

def main():
    # Get the input
    n = int(input())
    a = [int(x) for x in input().split()]

    # Solve
    print(solve(n, a))

def solve(n, a):
    # Sort a and get the unique elements
    unique_elements = sorted(set(a))

    # Find the number of groups and the number of elements in each group
    groups = len(unique_elements)
    elements = [0 for x in range(groups)]

    for i in range(n):
        elements[a[i]-1] += 1

    return max(elements) * len(elements)

if __name__ == '__main__':
    main()
