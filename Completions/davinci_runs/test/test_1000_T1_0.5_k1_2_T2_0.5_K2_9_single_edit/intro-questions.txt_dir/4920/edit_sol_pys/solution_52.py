

import sys

def main():
    string = sys.stdin.readline().strip()
    print(good_itineraries(string))

def good_itineraries(string):
    """
    :param string: string of lowercase letters
    :return: number of good itineraries
    """
    # good itineraries start with a unique letter
    # good itineraries end with a unique letter
    # good itineraries have at least 2 unique events
    # good itineraries don't have duplicates of the same event type
    # and then count the number of ways to fill in the middle with unique letters

    # first, find the first and the last unique letters
    first = None
    last = None
    # use a set to keep track of unique letters
    seen = set()
    for i, char in enumerate(string):
        # if we see a unique letter,
        # set that as the first unique letter
        if char not in seen:
            first = i
            seen.add(char)
        # if we see a letter that doesn't appear again,
        # set that as the last unique letter
        if char not in string[i+1:]:
            last = i
            break

    # there are no good itineraries if there is only one unique letter,
    # or if there are no unique events
    if first is None or last is None:
        return 0

    # now, count the number of ways to fill in the middle with unique letters
    # the middle can be filled with any characters,
    # as long as they don't repeat the first or last character
    # and as long as they don't repeat the same character
    # there are n - 2 positions to fill in, where n is the length of the string
    # and there are 26 - 2 characters to choose from, where 26 is the number of letters in the alphabet
    # so there are (n - 2) * (26 - 2) ways to fill in the middle with unique letters
    return (len(string) - 2) * (26 - 2) * 26

if __name__ == '__main__':
    main()
