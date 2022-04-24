

def main():
    # Get the number of test cases
    t = int(input())

    # Solve each test case
    for _ in range(t):
        # Get input
        n = int(input())
        a = [int(x) for x in input().split()]

        # Solve
        print(solve(n, a))

def solve(n, a):    
    # Sort a.
    a = sorted(a)    

    # Find the number of elements in each group.
    elements = [0 for _ in range(5)]
    for i in range(n):
        elements[a[i]-1] += 1

    # Find the number of elements in the largest group.
    max_elements = max(elements)

    # Find the number of groups that contain the largest number of elements.
    max_groups = 0
    for i in range(5):
        if elements[i] == max_elements:
            max_groups += 1

    # Return the answer
    return max_elements * max_groups

if __name__ == '__main__':
    main()
