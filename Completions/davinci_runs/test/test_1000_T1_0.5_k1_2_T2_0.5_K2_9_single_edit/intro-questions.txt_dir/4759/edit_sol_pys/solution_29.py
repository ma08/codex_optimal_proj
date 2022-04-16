

import sys

    """
    Returns the slugging percentage of a player.

    :param at_bats: a list of integers representing the number of bases a player has earned in each at-bat.
    :return: the slugging percentage of a player.
    """
def slugging_percentage(at_bats):
    total_bases = 0
    total_at_bats = 0
    for ab in at_bats:
        if ab >= 0:
            total_bases += ab
            total_at_bats += 1
    return total_bases / total_at_bats

def main():
    n = int(sys.stdin.readline().strip())
    at_bats = list(map(int, sys.stdin.readline().strip().split()))
    print(slugging_percentage(at_bats))

if __name__ == '__main__':
    main()
