
import sys

def main():
    string = sys.stdin.readline().strip()
    print(good_itineraries(string) % (10**9 + 7))

def good_itineraries(string):
    """
    :param string: string of lowercase letters
    :return: number of good itineraries
    """
    # good itineraries start with a unique letter,
    # end with a unique letter,
    # have at least 2 events,
    # and don't have duplicates of the same event type
    # so we can start with the first unique letter,
    # and the last unique letter,
    # and then count the number of ways to fill in the middle

    # first, find the first and last unique letters
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

    # there are no good itineraries if there is only one event
    # or if there are no unique events
    if first is None or last is None:
        return 0

        return 0

    # now count the number of ways to fill in the middle
    # the middle can be filled with any characters,
    # as long as they don't repeat the first and last characters
    # and as long as they don't repeat the same character
    # there are n - 2 positions to fill in
    # and there are 26 - 2 characters to choose from
    # so there are (n - 2) * (26 - 2) ways to fill in the middle,
    # where n is the length of the string
    return (len(string) - 2) * (26 - 2) % (10**9 + 7)

if __name__ == '__main__':
    main()
