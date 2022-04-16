

def get_min_rooms(preferences):
    """
    :param preferences: list of tuples, each tuple containing a lower and upper bound of temperature preference
    :return: minimum number of rooms required to make all the minions happy
    """
    # sort the preferences by the upper bound
    preferences.sort(key=lambda x: x[1])
    # set the first room to the first preference's upper bound
    rooms = [preferences[0][1]]
    # for each preference
    for lower, upper in preferences[1:]:
        # if the preference's lower bound is greater than the current room's temperature,
        # then place this minion in a new room
        if lower > rooms[-1]:
            rooms.append(upper)
    # return the number of rooms
    return len(rooms)

def main():
    n = int(input())
    preferences = []
    for _ in range(n):
        preferences.append(list(map(int, input().split())))
    print(get_min_rooms(preferences))

if __name__ == "__main__":
    main()
