

#TODO: fix the last test case, which is wrong

# This is a dynamic programming problem.
# For each stone, we can determine the possible speeds at which the car could have been traveling.
# Then, we can iterate through the stones and determine the possible speeds
# at which the car could have been traveling at that point.
# We can do this by taking the union of the possible speeds at the previous stone and the possible speeds
# at the current stone.

def get_possible_speeds(t, x, stone):
    # given the time and distance at which the car passed a stone,
    # returns the possible speeds at which the car could have been traveling
    speeds = set()
    for time in t[:stone]:
        for distance in x[:stone]:
            speeds.add(distance/(time*1.0) if time != 0 else float("inf"))
    return speeds

def get_possible_distances(t, x, stone):
    # given the time and distance at which the car passed a stone,
    # returns the possible distances between the first milestone and the second milestone
    distances = set()
    for time in t[:stone]:
        for distance in x[:stone]:
            distances.add(distance-time)
    return distances

def get_possible_speeds_at_stone(t, x, stone):
    # given the time and distance at which the car passed a stone,
    # returns the possible speeds at which the car could have been traveling at that point
    speeds_at_stone = get_possible_speeds(t, x, stone)
    return speeds_at_stone

def main():
    m, n = map(int, input().split())
    t = list(map(int, input().split()))
    x = list(map(int, input().split()))
    speeds = set()
    distances = set()
    for i in range(m):
        if i == 0:
            speeds_before = get_possible_speeds(t, x, i)
            distances_before = get_possible_distances(t, x, i)
        else:
            speeds_before = speeds
            distances_before = distances
        speeds = get_possible_speeds_at_stone(t, x, i)
        distances = get_possible_distances(t, x, i)
        distances.update(distances_before)
    print(len(speeds))
    print(" ".join(map(str, sorted(distances))))

main()
