

def get_min_rooms(preferences):
    """
    :param preferences: list of tuples, each tuple containing a lower and upper bound of temperature preference
    :return: minimum number of rooms required to make all the minions happy
    """


def main():
    n = int(input())
    preferences = []
    for _ in range(n):
        preferences.append(list(map(int, input().split())))
    print(get_min_rooms(preferences))

if __name__ == "__main__":
    main()
