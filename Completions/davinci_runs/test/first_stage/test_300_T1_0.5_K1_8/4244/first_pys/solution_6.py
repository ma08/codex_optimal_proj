

import sys

def get_min_stamina(locations):
    """
    returns the minimum total stamina the N people have to spend
    :param locations: list of locations of N people
    :return: minimum total stamina the N people have to spend
    """
    locations.sort()
    return sum([(locations[i+1] - locations[i])**2 for i in range(len(locations) - 1)])

def main():
    n = int(sys.stdin.readline())
    locations = [int(x) for x in sys.stdin.readline().split()]
    print(get_min_stamina(locations))

if __name__ == '__main__':
    main()