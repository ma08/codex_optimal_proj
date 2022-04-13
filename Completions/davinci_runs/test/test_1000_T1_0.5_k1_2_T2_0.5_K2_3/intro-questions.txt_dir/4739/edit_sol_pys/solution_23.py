

# Find the sum of all possible distances between the first and second milestones seen.
# Sort the list of milestones, and then find the sum of all distances between the first and second milestones seen.
def main():
    # Get the number of milestones seen and the total number of milestones
    M, N = map(int, input().split())
    # Get the times at which each milestone was seen
    T = list(map(int, input().split()))
    # Get the distances between each milestone
    X = list(map(int, input().split()))
    # Sort the list of milestones
    X.sort()
    # Find the sum of all possible distances between the first and second milestones seen
    # Find the possible distances for each milestone seen
    sum_of_distances = 0
    for i in range(M):
        # Find the distances between the first milestone seen and the milestone seen at time T[i]
        distances = [X[j] - X[0] for j in range(i+1)]
        # If there is a distance that is greater than T[i], then it is not possible to reach the milestone
        # by time T[i]
        if distances[-1] > T[i]:
            continue
        # Otherwise, add the sum of the distances
        sum_of_distances += sum(distances)
    # Print the sum of the possible distances
    print(sum_of_distances)

main()
