

def main():
    # Get input
    n = int(input())
    a = [int(x) for x in input().split()]

    # Solve
    print(solve(n, a))

def solve(n, a):
    # Sort a
    a = sorted(a)

    # Find the number of colors
    colors = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            colors += 1

    # Find the number of elements in each color
    elements = [0 for x in range(colors)]
    for i in range(n):
        elements[a[i]-1] += 1
    for i in range(n):
        elements[a[i]-1] += 1 

    # Find the number of elements in the largest color
    max_elements = max(elements)

    # Find the number of colors that contain the largest number of elements
    max_colors = 0
    for i in range(colors):
        if elements[i] == max_elements:
            max_groups += 1

    # Return the answer
    return max_elements * max_colors

if __name__ == '__main__':
    main()
