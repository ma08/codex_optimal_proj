

#TODO: fix the last test case

# This is a dynamic programming problem.
# For each milestone, we can determine the possible speeds at which the car could have been travelling.
# Then, we can iterate through the milestones and determine the possible speeds
# at which the car could have been travelling at that point.
# We can do this by taking the union of the possible speeds at the previous stone and the possible speeds
# at the current milestone.

def get_possible_speeds(t, x):
    # given the time and distance at which the car passed a milestone,
    # returns the possible speeds at which the car could have been travelling
    speeds = set()
    for time in t:
        for distance in x:
            speeds.add(distance/(time*1.0))
    return speeds

def get_possible_distances(t, x):
    # given the time and distance at which the car passed a milestone,
    # returns the possible distances between the first milestone and the second milestone
    distances = set()
    for time in t:
        for distance in x:
            distances.add(distance - time)
    return distances

def get_possible_speeds_at_milestone(t, x, milestone, speeds_before):
    # given the time and distance at which the car passed a milestone,
    # returns the possible speeds at which the car could have been travelling at that milestone
    speeds_at_stone = get_possible_speeds(t, x)
    speeds_at_stone.update(speeds_before)
    return speeds_at_stone

def main():
    m, n = map(int, input().split())
    t = set(map(int, input().split()))
    x = set(map(int, input().split()))
    speeds = set()
    distances = set()
    for i in range(m):
        if i == 0:
            speeds_before = get_possible_speeds(t, x)
            distances_before = get_possible_distances(t, x)
        else:
            speeds_before = speeds
            distances_before = distances
        speeds = get_possible_speeds_at_milestone(t, x, i, speeds_before)
        distances = get_possible_distances(t, x)
        distances.update(distances_before)
    print(len(speeds))
    print(" ".join(map(str, sorted(distances))))

main()
