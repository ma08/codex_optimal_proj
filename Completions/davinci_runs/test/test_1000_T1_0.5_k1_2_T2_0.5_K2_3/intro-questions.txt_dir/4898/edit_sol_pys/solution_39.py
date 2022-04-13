

def get_min_rooms(preferences):
    """
    :param preferences: list of tuples, each tuple containing a lower and upper bound of temperature preference
    :return: minimum number of rooms required to make all the minnions happy
    """
    # sort the preferences by the lower bound
    preferences.sort(key=lambda x: x[1])
    # set the first room to the first preference's lower bound
    rooms = [preferences[0][0]]
    # for each preference
    for preference in preferences[1:]:
        # if the preference's upper bound is greater than the current room's temperature,
        # then place this minnion in a new room
        if preference[1] > rooms[-1]:
            rooms.append(preference[0])
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
