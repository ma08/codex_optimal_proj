

def main():
    # Get input and split it
    line = input().split()

    # Solve
    print(solve(line))

def solve(line):
    # Sort line
    line = sorted(line)

    # Find the number of groups
    groups = 1
    for i in range(len(line)-1):
        if line[i] != line[i+1]:
            groups += 1

    # Find the number of element in each group
    elements = [0 for x in range(groups)] # elements[i] = number of elements in group i
    for i in range(len(line)):
        elements[line[i]-1] += 1

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
