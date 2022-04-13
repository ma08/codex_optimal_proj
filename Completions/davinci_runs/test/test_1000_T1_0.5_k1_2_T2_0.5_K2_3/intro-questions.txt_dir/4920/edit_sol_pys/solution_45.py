

import sys

def main():
    string = sys.stdin.readline().strip()
    print(good_itineraries(string))

def good_itineraries(string):
    https://www.hackerrank.com/challenges/good-itineraries/problem
    """
    :param string: string of lowercase letters
    :return: number of good itineraries
    """
    # Good itineraries start with a unique letter
    # Good itineraries end with a unique letter
    # Good itineraries have at least 2 events
    # Good itineraries don't have duplicates of the same event
    # So we can start with the first unique letter, and the last unique letter
    # And then count the number of ways to fill in the middle

    # First, find the first and the last unique letters
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

    # There are no good itineraries if there is only one event,
    # Or if there are no unique events
    if first is None or last is None:
        return 0

    # Now, count the number of ways to fill in the middle
    # The middle can be filled with any characters,
    # As long as they don't repeat the first or last character
    # And as long as they don't repeat the same character
    # There are n - 2 positions to fill in,
    # And there are 26 - 2 characters to choose from
    # So there are (n - 2) * (26 - 2) ways to fill in the middle
    return (len(string) - 2) * (26 - 2)

if __name__ == '__main__':
    main()
