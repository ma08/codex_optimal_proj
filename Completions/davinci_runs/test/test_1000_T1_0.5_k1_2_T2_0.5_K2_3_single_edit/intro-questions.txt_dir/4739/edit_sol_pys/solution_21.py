

# The problem is equivalent to finding all possible distances between the first and second milestones seen
# Sort the list of milestones, and then find all differences between the first and second milestones seen at each time
def main():
    # Get the number of milestones seen and the total number of milestones
    M, N = map(int, input().split())
    # Get the times at which each milestone was seen
    T = list(map(int, input().split()))
    # Get the distances between each milestone
    X = list(map(int, input().split()))
    # Sort the list of milestones
    X.sort()
    # Find all possible distances between the first and second milestones seen at each time
    # Find the possible distances for each milestone seen
    possible_distances = []
    for i in range(M):
        # Find the distances between the first milestone seen and the milestone seen at time T[i]
        distances = [X[j] - X[0] for j in range(i+1)]
        # If there is a distance that is greater than T[i], then it is not possible to reach the milestone
        # by time T[i]
        if distances[-1] > T[i]:
            continue
        # Otherwise, add the distances
        possible_distances += distances
    # Sort the possible distances and find the unique possible distances
    possible_distances.sort()
    possible_distances = list(set(possible_distances))
    # Print the number of possible distances
    print(len(possible_distances))
    # Print the possible distances
    print(*possible_distances)

main()
