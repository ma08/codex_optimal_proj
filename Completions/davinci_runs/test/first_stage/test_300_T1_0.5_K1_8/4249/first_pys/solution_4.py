

import sys

def readline_int_list():
    return [int(x) for x in sys.stdin.readline().split()]

def solve(m, caffeine_dosages):
    """
    caffeine_dosages is a list of caffeine dosages
    """
    # we can simulate the process of writing coursework and drinking coffee
    # in a single pass
    # we can only drink coffee that is not yet drunk
    caffeine_dosages.sort(reverse=True)
    caffeine_dosages_length = len(caffeine_dosages)
    remaining_pages = m
    remaining_cups = caffeine_dosages_length
    days = 0
    while remaining_pages > 0 and remaining_cups > 0:
        # we can drink the remaining cups of coffee and write some pages
        days += 1
        # we can drink the remaining cups of coffee
        # we can write at most remaining_cups pages
        remaining_pages -= remaining_cups
        # remove the caffeine dosages that we have already drunk
        # we can only drink coffee that is not yet drunk
        caffeine_dosages = caffeine_dosages[remaining_cups:]
        remaining_cups = len(caffeine_dosages)
    if remaining_pages > 0:
        # we cannot write the remaining pages
        return -1
    else:
        # we can write all the pages
        return days

def main():
    n, m = readline_int_list()
    caffeine_dosages = readline_int_list()
    assert(len(caffeine_dosages) == n)
    print(solve(m, caffeine_dosages))

if __name__ == "__main__":
    main()