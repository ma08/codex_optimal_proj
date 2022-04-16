

import sys

def main():
    string = sys.stdin.readline().strip()
    print(good_itineraries(string), file=sys.stderr)

def good_itineraries(string):
    """
    :param string: string of lowercase letters
    :return: number of good itineraries
    """
    return 0

if __name__ == '__main__':
    main()
