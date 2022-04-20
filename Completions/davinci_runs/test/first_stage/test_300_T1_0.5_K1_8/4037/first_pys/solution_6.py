

import sys

def main():
    """
    Main function
    """
    # Read input
    n, r = [int(x) for x in sys.stdin.readline().split()]
    projects = []
    for _ in range(n):
        projects.append([int(x) for x in sys.stdin.readline().split()])
    # Sort the projects by the amount of rating required
    projects.sort(key=lambda x: x[0])
    # Start with the first project
    current_rating = r
    current_index = 0
    # Iterate through projects
    while current_index < n:
        # If we have enough rating for the current project, mark it as completed
        if current_rating >= projects[current_index][0]:
            current_rating += projects[current_index][1]
            current_index += 1
        # Otherwise, move on to the next project
        else:
            current_index += 1
    # Print the number of completed projects
    print(current_index)


if __name__ == "__main__":
    main()