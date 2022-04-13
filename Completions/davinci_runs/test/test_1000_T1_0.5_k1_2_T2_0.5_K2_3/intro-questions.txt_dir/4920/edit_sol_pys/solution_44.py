

import sys

def main():
    string = sys.stdin.readline().strip()
    print(good_itineraries(string))

def good_itineraries(string):
    """
    :param string: string of lowercase letters
    :return: number of good itineraries
    """
    # good itineraries start with a unique character
    # good itineraries end with a unique character
    # good itineraries have at least 2 characters
    # good itineraries don't have duplicates of the same character
    # so we can start with the first unique character, and the last unique character
    # and then count the number of ways to fill in the rest

    # first, find the first and the last unique characters
    first = None
    last = None
    seen = set()
    for i, char in enumerate(string):
        if char not in seen:
            first = i
            seen.add(char)
        if char not in string[i+1:]:
            last = i
            break

    # there are no good itineraries if there is only one event,
    # or if there are no unique events
    if first is None or last is None:
        return 0

    # now, count the number of ways to fill in the middle
    # the middle can be filled with any characters,
    # as long as they don't repeat the first or last character
    # and as long as they don't repeat the same character
    # there are n - 2 positions to fill in,
    # and there are 26 - 2 characters to choose from
    # so there are (n - 2) * (26 - 2) ways to fill in the middle
    return (len(string) - 2) * (26 - 2)

if __name__ == '__main__':
    main()
