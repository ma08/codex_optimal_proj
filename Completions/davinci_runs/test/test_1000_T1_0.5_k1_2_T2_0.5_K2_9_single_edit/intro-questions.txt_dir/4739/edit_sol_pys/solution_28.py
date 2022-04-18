

def main():
    """
    Calculates the number of possible speeds at which the car could have been travelling given the number of milestones seen,
    the times at which they were seen, and the distances along the road of each milestone.

    :return: None
    """
    # Get the number of milestones seen as well as the total number of milestones along the road
    milestones_seen, total_milestones = map(int, input().split())

    # Get the times at which the milestones were seen
    times = list(map(int, input().split()))

    # Get the distances along the road of each milestone
    distances = list(map(int, input().split()))

    # Get the number of possible speeds at which the car could have been travelling
    num_speeds = get_num_speeds(milestones_seen, total_milestones, times, distances)

    # Get the possible distances between the first milestone seen and the second milestone seen
    distances_between = get_distances_between(milestones_seen, total_milestones, distances)

    # Print the number of possible speeds at which the car could have been travelling
    print(num_speeds)

    # Print the possible distances between the first milestone seen and the second milestone seen
    print(" ".join(map(str, distances_between)))

def get_num_speeds(milestones_seen, total_milestones, times, distances):
    """
    Calculates the number of possible speeds at which the car could have been travelling given the number of milestones seen,
    the times at which they were seen, and the distances along the road of each milestone.

    :param milestones_seen: The number of milestones seen
    :param total_milestones: The total number of milestones along the road
    :param times: The times at which the milestones were seen
    :param distances: The distances along the road of each milestone
    :return: The number of possible speeds at which the car could have been travelling
    """
    # Define a set to store the possible speeds at which the car could have been travelling
    speeds = set()

    # For each milestone seen
    for i in range(milestones_seen):
        # For each milestone not seen
        for j in range(milestones_seen, total_milestones):
            # Calculate the speed at which the car could have been travelling
            speed = (distances[j] - distances[i]) / (times[j] - times[i])

            # Add the speed to the set of possible speeds at which the car could have been travelling
            speeds.add(speed)

    # Return the number of possible speeds at which the car could have been travelling
    return len(speeds)

def get_distances_between(milestones_seen, total_milestones, distances):
    """
    Calculates the possible distances between the first milestone seen and the second milestone seen given the number of
    milestones seen, the times at which they were seen, and the distances along the road of each milestone.

    :param milestones_seen: The number of milestones seen
    :param total_milestones: The total number of milestones along the road
    :param distances: The distances along the road of each milestone
    :return: The possible distances between the first milestone seen and the second milestone seen
    """
    # Define a list to store the possible distances between the first milestone seen and the second milestone seen
    distances_between = []

    distances_between = []

    # For each milestone
    for i in range(total_milestones - 1):
        # Calculate the distance between the current milestone and the next milestone
        distance = distances[i + 1] - distances[i]

        # Add the distance to the list of possible distances between the first milestone seen and the second milestone seen
        distances_between.append(distance)

    # Return the possible distances between the first milestone seen and the second milestone seen
    return sorted(distances_between)

if __name__ == "__main__":
    main()
