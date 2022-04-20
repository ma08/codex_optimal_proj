

def main():
    # Get input
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split() for y in range(n)]

    # Solve
    print(solve(n, m, a))

def solve(n, m, a):
    # Sort a
    a = sorted(a)

    # Find the number of segments
    segments = 0
    for i in range(n):
        if a[i] == 1:
            segments += 1

    # elements = [0 for x in range(groups)]
    # for i in range(n):
    #     elements[a[i]-1] += 1

    # # Find the number of elements in the largest group
    # max_elements = max(elements)

    # # Find the number of groups that contain the largest number of elements
    # max_groups = 0
    # for i in range(groups):
    #     if elements[i] == max_elements:
    #         max_groups += 1

    # Return the answer
    return segments

if __name__ == '__main__':
    main()
