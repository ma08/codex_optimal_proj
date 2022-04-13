

def get_min_rooms(preference):
    """
    :param preference: list of tuples, each tuple containing a lower and upper bound of temperature preference
    :return: minimum number of rooms required to make all the minions happy
    """
    # sort the preferences by the upper bound
    preference.sort(key=lambda preference: preference[1])
    # set the first room to the first preference's upper bound
    rooms = [preference[0][1]]
    # for each preference
    for preference in preference[1:]:
        # if the preference's lower bound is greater than the current room's temperature,
        # then place this minion in a new room
        if preference[0] > rooms[-1]:
            rooms.append(preference[1])
    # return the number of rooms
    return len(rooms)

def main():
    n = int(input())
    preference = []
    for _ in range(n):
        preference.append(list(map(int, input().split())))
    print(get_min_rooms(preference))

if __name__ == "__main__":
    main()
